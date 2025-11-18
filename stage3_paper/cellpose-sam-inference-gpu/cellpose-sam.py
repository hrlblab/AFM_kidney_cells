#!/usr/bin/env python3
"""
Run Cellpose-SAM for cellular segmentation on a folder of images.

This script is adapted from the official Cellpose-SAM Colab notebook by Marius Pachitariu, Michael Rariden, and Carsen Stringer.
It supports batch processing of .png or .tif images using GPU acceleration.

pip install git+https://github.com/mouseland/cellpose.git
pip install matplotlib tqdm numpy

Usage:
    python run_cellpose_sam.py --input_dir /path/to/images --output_dir /path/to/output --ext .png
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from tqdm import trange
from cellpose import models, io, utils, core


def main(args):
    # === CHECK GPU ===
    io.logger_setup()
    if not core.use_gpu():
        raise RuntimeError("No GPU detected. Please run this script on a machine with CUDA/MPS GPU enabled.")

    # === PATH SETUP ===
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # === PARAMETERS ===
    image_ext = args.ext
    flow_threshold = args.flow_threshold
    cellprob_threshold = args.cellprob_threshold
    tile_norm_blocksize = args.tile_norm_blocksize

    # === LOAD FILES ===
    files = sorted([f for f in input_dir.glob(f"*{image_ext}") if "_masks" not in f.name and "_flows" not in f.name])
    if len(files) == 0:
        raise FileNotFoundError(f"No {image_ext} files found in {input_dir}")

    print(f" Found {len(files)} images in {input_dir}")

    # === INIT MODEL ===
    print(" Loading Cellpose-SAM model...")
    model = models.CellposeModel(gpu=True) # load cellpose-sam (cpsam) by default: https://cellpose.readthedocs.io/en/latest/api.html#cellposemodel

    # === LOOP OVER IMAGES ===
    for i in trange(len(files), desc="Processing images"):
        img_path = files[i]
        img = io.imread(img_path)

        # Run segmentation
        masks, flows, styles = model.eval(
            img,
            batch_size=32,
            flow_threshold=flow_threshold,
            cellprob_threshold=cellprob_threshold,
            normalize={"tile_norm_blocksize": tile_norm_blocksize},
        )

        # Normalize for display
        img_rgb = img.astype(np.float32)
        if img_rgb.max() > 1.0:
            img_rgb /= 255.0

        # Plot original image with predicted outlines
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.imshow(img_rgb)
        outlines = utils.outlines_list(masks)
        for o in outlines:
            ax.plot(o[:, 0], o[:, 1], color="#39FF14", linewidth=3.0)
        ax.axis("off")

        # Save overlay and masks
        overlay_path = output_dir / f"{img_path.stem}_overlay.png"
        mask_path = output_dir / f"{img_path.stem}_masks{image_ext}"

        plt.savefig(overlay_path, dpi=300, bbox_inches="tight")
        plt.close(fig)

        # io.imsave(mask_path, masks.astype(np.uint16))

    print(f" Done! Results saved in {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Cellpose-SAM segmentation")
    parser.add_argument("--input_dir", type=str, required=True, help="Path to folder with input images")
    parser.add_argument("--output_dir", type=str, required=True, help="Path to save outputs")
    parser.add_argument("--ext", type=str, default=".png", help="Image file extension (e.g., .png or .tif)")
    parser.add_argument("--flow_threshold", type=float, default=1.0, help="Flow threshold for segmentation")
    parser.add_argument("--cellprob_threshold", type=float, default=0.0, help="Cell probability threshold")
    parser.add_argument("--tile_norm_blocksize", type=int, default=150, help="Block size for brightness normalization")
    args = parser.parse_args()

    main(args)
