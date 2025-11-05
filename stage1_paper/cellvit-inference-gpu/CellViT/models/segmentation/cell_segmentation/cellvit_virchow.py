# -*- coding: utf-8 -*-
#
# CellViT-Virchow model
#
# @ Fabian Hörst, fabian.hoerst@uk-essen.de
# Institute for Artifical Intelligence in Medicine,
# University Medicine Essenfrom pathlib import Pathfrom pathlib import Path

from typing import Union
from pathlib import Path

import torch
import torch.nn as nn
from .cellvit import CellViT
from .backbones import ViTCellViTVirchow
import torch.nn.functional as F


from .utils import Conv2DBlock, Deconv2DBlock


class CellViTVirchow(CellViT):
    """CellViT with ViT-Virchow backbone settings

    Virchow Links:
        Paper: https://doi.org/10.1038/s41591-024-03141-0
        HuggingFace: https://huggingface.co/paige-ai/Virchow

    Args:
        model_virchow_path (Union[Path, str]): Path to Virchow checkpoint
        num_nuclei_classes (int): Number of nuclei classes (including background)
        num_tissue_classes (int): Number of tissue classes
        drop_rate (float, optional): Dropout in MLP. Defaults to 0.
        attn_drop_rate (float, optional): Dropout for attention layer in backbone ViT. Defaults to 0.
        drop_path_rate (float, optional): Dropout for skip connection . Defaults to 0.
    """

    def __init__(
        self,
        model_virchow_path: Union[Path, str],
        num_nuclei_classes: int,
        num_tissue_classes: int,
        drop_rate: float = 0,
        attn_drop_rate: float = 0,
        drop_path_rate: float = 0,
    ):
        super(CellViT, self).__init__()
        self.img_size = 224
        self.patch_size = 14
        self.embed_dim = 1280
        self.depth = 32
        self.num_heads = 16
        self.qkv_bias = True
        self.extract_layers = [8, 16, 24, 32]
        self.input_channels = 3
        self.mlp_ratio = 5.3375
        self.drop_rate = 0
        self.num_tissue_classes = num_tissue_classes
        self.num_nuclei_classes = num_nuclei_classes
        self.model_virchow_path = model_virchow_path

        # add internal image size for the two different sizes of 256 and 1024 pixels
        self.input_rescale_dict = {256: 252, 1024: 1022}
        regression_loss = False

        self.encoder = ViTCellViTVirchow(
            extract_layers=self.extract_layers,
            num_classes=num_tissue_classes,
        )

        if self.embed_dim < 512:
            self.skip_dim_11 = 256
            self.skip_dim_12 = 128
            self.bottleneck_dim = 312
        else:
            self.skip_dim_11 = 512
            self.skip_dim_12 = 256
            self.bottleneck_dim = 512

        # version with shared skip_connections
        self.decoder0 = nn.Sequential(
            Conv2DBlock(3, 32, 3, dropout=self.drop_rate),
            Conv2DBlock(32, 64, 3, dropout=self.drop_rate),
        )  # skip connection after positional encoding, shape should be H, W, 64
        self.decoder1 = nn.Sequential(
            Deconv2DBlock(self.embed_dim, self.skip_dim_11, dropout=self.drop_rate),
            Deconv2DBlock(self.skip_dim_11, self.skip_dim_12, dropout=self.drop_rate),
            Deconv2DBlock(self.skip_dim_12, 128, dropout=self.drop_rate),
        )  # skip connection 1
        self.decoder2 = nn.Sequential(
            Deconv2DBlock(self.embed_dim, self.skip_dim_11, dropout=self.drop_rate),
            Deconv2DBlock(self.skip_dim_11, 256, dropout=self.drop_rate),
        )  # skip connection 2
        self.decoder3 = nn.Sequential(
            Deconv2DBlock(self.embed_dim, self.bottleneck_dim, dropout=self.drop_rate)
        )  # skip connection 3

        self.regression_loss = regression_loss
        offset_branches = 0
        if self.regression_loss:
            offset_branches = 2
        self.branches_output = {
            "nuclei_binary_map": 2 + offset_branches,
            "hv_map": 2,
            "nuclei_type_maps": self.num_nuclei_classes,
        }

        self.nuclei_binary_map_decoder = self.create_upsampling_branch(
            2 + offset_branches
        )  # todo: adapt for helper loss
        self.hv_map_decoder = self.create_upsampling_branch(
            2
        )  # todo: adapt for helper loss
        self.nuclei_type_maps_decoder = self.create_upsampling_branch(
            self.num_nuclei_classes
        )

        # Don't automatically load pretrained encoder - let the inference script handle it
        # self.load_pretrained_encoder(self.model_virchow_path)

    def _forward_upsample(
        self,
        z0: torch.Tensor,
        z1: torch.Tensor,
        z2: torch.Tensor,
        z3: torch.Tensor,
        z4: torch.Tensor,
        branch_decoder: nn.Sequential,
        rescale_value: int,
    ) -> torch.Tensor:
        """Forward upsample branch

        Args:
            z0 (torch.Tensor): Highest skip
            z1 (torch.Tensor): 1. Skip
            z2 (torch.Tensor): 2. Skip
            z3 (torch.Tensor): 3. Skip
            z4 (torch.Tensor): Bottleneck
            branch_decoder (nn.Sequential): Branch decoder network
            rescale_value (int): Value for rescaling due to different patch sizes
        Returns:
            torch.Tensor: Branch Output
        """
        b4 = branch_decoder.bottleneck_upsampler(z4)
        b3 = self.decoder3(z3)
        b3 = branch_decoder.decoder3_upsampler(torch.cat([b3, b4], dim=1))
        b2 = self.decoder2(z2)
        b2 = branch_decoder.decoder2_upsampler(torch.cat([b2, b3], dim=1))
        b1 = self.decoder1(z1)
        b1 = branch_decoder.decoder1_upsampler(torch.cat([b1, b2], dim=1))
        b1 = F.interpolate(
            b1,
            size=(rescale_value, rescale_value),
            mode="bilinear",
            align_corners=False,
        )
        b0 = self.decoder0(z0)
        b0 = F.interpolate(
            b0,
            size=(rescale_value, rescale_value),
            mode="bilinear",
            align_corners=False,
        )
        branch_output = branch_decoder.decoder0_header(torch.cat([b0, b1], dim=1))

        return branch_output

    def load_pretrained_encoder(self, model_virchow_path: Union[Path, str]):
        """Load pretrained UNI from provided path

        Args:
            model_virchow_path (str): Path to Virchow (ViT-H foundation model)
        """
        if model_virchow_path is None:
            print(f"No checkpoint provided!")
        else:
            state_dict = torch.load(str(model_virchow_path), map_location="cpu")
            msg = self.encoder.load_state_dict(state_dict, strict=False)
            print(f"Loading checkpoint: {msg}")

    def forward(self, x: torch.Tensor, retrieve_tokens: bool = False) -> dict:
        """Forward pass

        Args:
            x (torch.Tensor): Images in BCHW style
            retrieve_tokens (bool, optional): If tokens of ViT should be returned as well. Defaults to False.

        Returns:
            dict: Output for all branches:
                * tissue_types: Raw tissue type prediction. Shape: (B, num_tissue_classes)
                * nuclei_binary_map: Raw binary cell segmentation predictions. Shape: (B, 2, H, W)
                * hv_map: Binary HV Map predictions. Shape: (B, 2, H, W)
                * nuclei_type_map: Raw binary nuclei type preditcions. Shape: (B, num_nuclei_classes, H, W)
                * [Optional, if retrieve tokens]: tokens
                * [Optional, if regression loss]:
                * regression_map: Regression map for binary prediction. Shape: (B, 2, H, W)
        """
        out_dict = {}
        bs = x.shape[0]
        input_shape = x.shape[2]
        rescale_value = self.input_rescale_dict[input_shape]

        x = F.interpolate(x, size=(rescale_value, rescale_value), mode="area")
        classifier_logits, _, z = self.encoder(x)
        out_dict["tissue_types"] = classifier_logits

        z0, z1, z2, z3, z4 = x, *z

        # performing reshape for the convolutional layers and upsampling (restore spatial dimension)
        patch_dim = [int(d / 14) for d in [x.shape[-2], x.shape[-1]]]
        z4 = z4[:, 1:, :].transpose(-1, -2).view(-1, self.embed_dim, *patch_dim)
        z3 = z3[:, 1:, :].transpose(-1, -2).view(-1, self.embed_dim, *patch_dim)
        z2 = z2[:, 1:, :].transpose(-1, -2).view(-1, self.embed_dim, *patch_dim)
        z1 = z1[:, 1:, :].transpose(-1, -2).view(-1, self.embed_dim, *patch_dim)

        if self.regression_loss:
            nb_map = self._forward_upsample(
                z0, z1, z2, z3, z4, self.nuclei_binary_map_decoder, input_shape
            )
            out_dict["nuclei_binary_map"] = nb_map[:, :2, :, :]
            out_dict["regression_map"] = nb_map[:, 2:, :, :]
        else:
            out_dict["nuclei_binary_map"] = self._forward_upsample(
                z0, z1, z2, z3, z4, self.nuclei_binary_map_decoder, input_shape
            )
        out_dict["hv_map"] = self._forward_upsample(
            z0, z1, z2, z3, z4, self.hv_map_decoder, input_shape
        )
        out_dict["nuclei_type_map"] = self._forward_upsample(
            z0, z1, z2, z3, z4, self.nuclei_type_maps_decoder, input_shape
        )
        if retrieve_tokens:
            out_dict["tokens"] = z4

        return out_dict
