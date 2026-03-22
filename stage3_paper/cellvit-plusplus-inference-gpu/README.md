# Class Agnostic Patch-level CellViT++ Inference 

***What is new in CellViT++***: Apart from backbone support for HIPT-256, SAM-H, CellViT++ also supplies `Virchow` backbone.

[***Python script***](CellViT-plus-plus/cell_segmentation/inference/inference_cellvit_experiment_ca.py) we run inference is at:
```bash
CellViT-plus-plus/cell_segmentation/inference/inference_cellvit_experiment_ca.py
``` 
Here, **`ca`** stands for **class-agnostic** inference for our dataset.

## Requirements 

### System 

- CUDA-compatible GPU 

- NVIDIA GPU drivers

- Python 3.9.7 (Based on original CellViT [repo](CellViT/README(original-cellvit-paper).md) installation)

### Installation 

Ensure successful loading packages/libraries of [inference_cellvit_experiment_ca.py](CellViT/cell_segmentation/inference/inference_cellvit_experiment_ca.py).

```bash
conda create -n <env_name> python=3.9.7
conda activate <env_name>

pip install -r requirements.txt
```
The `requirements.txt` file can be also found in the original CellViT [<ins>GitHub repo</ins>](https://github.com/TIO-IKIM/CellViT/tree/main) (link here). 

Installation should be straightforward, just ensure the inference script loads all required packages successfully.

## Usage 

### Dataset Prep

Simply place your image patches into a folder (e.g., the 512x512 PAS patches (40x) in the [**examples**](../examples/) directory).


### Model Checkpoints

We evaluated these backbones in our paper. These CellViT++ checkpoints can be downloaded from [**Google Drive**](https://drive.google.com/drive/folders/1aD4nvhK-fhjezHzcRaSsF-wqqFv46qW0?usp=sharing)  
- CellViT-SAM-H-x40-AMP
- CellViT-256-x40-AMP (HIPT)
- CellViT-Virchow-x40

Download the checkpoint (.pth) that will be used and place in a folder, like `dummpy_checkpoints`.


### Run the Inference Script 

```bash
python /path/to/CellViT/cell_segmentation/inference/inference_cellvit_experiment_ca.py \
    --gpu 0 \
    --model /path/to/checkpoint.pth \
    --patching True \
    --overlap 0 \
    --dataset /path/to/dataset_folder \
    --outdir /path/to/output \
    --plots False
```

#### Note:

`--plots` defaults to `False`. When `False`, all models save only the predicted instance mask as a `.npy` file.

> **Known issue:** `CellViTVirchow` produces incorrect contour visualizations (color artifacts in the PNG) due to a normalization mismatch. The `.npy` mask is unaffected. Use a separate visualization script for `CellViTVirchow` outputs.

### Visualize Instance Masks

Use [**visualize_instance_mask.py**](visualize_instance_mask.py) to convert a predicted `.npy` mask into a color-coded PNG:

```bash
# output auto-named as *_instance_seg.png
python visualize_instance_mask.py --input /path/to/patch_contours.npy

# or specify output path
python visualize_instance_mask.py --input /path/to/patch_contours.npy --output /path/to/out.png
```

## License

This script is provided under the MIT License. Please see the LICENSE file for details.

## Citation

If you find this repository useful, please consider giving a ⭐ and citing our papers:

```bibtex
@inproceedings{guo2025assessment,
  title={Assessment of cell nuclei AI foundation models in kidney pathology},
  author={Guo, Junlin and Lu, Siqi and Cui, Can and Deng, Ruining and Yao, Tianyuan and Tao, Zhewen and Lin, Yizhe and Lionts, Marilyn and Liu, Quan and Xiong, Juming and others},
  booktitle={Medical Imaging 2025: Image Perception, Observer Performance, and Technology Assessment},
  volume={13409},
  pages={76--82},
  year={2025},
  organization={SPIE}
}


@article{guo2025evaluating,
  title={Evaluating cell AI foundation models in kidney pathology with human-in-the-loop enrichment},
  author={Guo, Junlin and Lu, Siqi and Cui, Can and Deng, Ruining and Yao, Tianyuan and Tao, Zhewen and Lin, Yizhe and Lionts, Marilyn and Liu, Quan and Xiong, Juming and others},
  journal={Communications Medicine},
  volume={5},
  number={1},
  pages={495},
  year={2025},
  publisher={Nature Publishing Group}
}


@article{wang2025evaluating,
  title={Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models},
  author={Wang, Runchen and Guo, Junlin and Lu, Siqi and Deng, Ruining and Lu, Zhengyi and Zhu, Yanfan and Yang, Yuechen and Qu, Chongyu and Wang, Yu and Zhao, Shilin and others},
  journal={arXiv preprint arXiv:2510.01287},
  year={2025}
}
```
