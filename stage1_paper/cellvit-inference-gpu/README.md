# Class Agnostic Patch-level CellViT Inference 

CellViT model inference on image patches, with backbone support for HIPT-256, SAM-H in both 20X and 40X resolution. 
The [python script](CellViT/cell_segmentation/inference/inference_cellvit_experiment_ca.py) we run inference is at:
```bash
CellViT/cell_segmentation/inference/inference_cellvit_experiment_ca.py
``` 
Here, **`ca`** stands for **class-agnostic** inference for our kidney dataset.

## Requirements 

### System 

- CUDA-compatible GPU 

- NVIDIA GPU drivers

- Python 3.9.7 (Based on original CellViT [repo](CellViT/README(original-cellvit-paper).md) installation)

### Installation 

Ensure successful loading packages/libraries of [inference_cellvit_experiment_ca.py](CellViT/cell_segmentation/inference/inference_cellvit_experiment_ca.py).


#### Option 1: Use Conda (Recommended)

```bash
conda env create -f environment.yml
conda activate <env_name>
```

#### Option 2: Use Pip 

```bash
conda create -n <env_name> python=3.9.7
conda activate <env_name>

pip install -r requirements.txt
```
The [enrionment.yml](CellViT/environment.yml) and [requirements.txt](CellViT/requirements.txt) are provided in CellViT folder.

## Usage 

### Dataset Prep

Simply place your image patches into a folder (e.g., the 512x512 PAS patches (40x) in the [**examples**](../examples/) directory).


### Model Checkpoints

The CellViT pre-trained checkpoint from CellViT paper can be found: 
- [CellViT-SAM-H](https://drive.google.com/uc?export=download&id=1MvRKNzDW2eHbQb5rAgTEp6s2zAXHixRV) 🚀
- [CellViT-256](https://drive.google.com/uc?export=download&id=1tVYAapUo1Xt8QgCN22Ne1urbbCZkah8q) (We used this HIPT-256 for evaluation)
- [CellViT-SAM-H-x20](https://drive.google.com/uc?export=download&id=1wP4WhHLNwyJv97AK42pWK8kPoWlrqi30)
- [CellViT-256-x20](https://drive.google.com/uc?export=download&id=1w99U4sxDQgOSuiHMyvS_NYBiz6ozolN2)

Download the checkpoint (.pth) that will be used and place in a folder, like `model_checkpoints`.


### Run the Inference Script 


```bash
python /path/to/CellViT/cell_segmentation/inference/inference_cellvit_experiment_ca.py \
    --gpu 0 \
    --model /path/to/checkpoint.pth \
    --patching True \
    --overlap 0 \
    --dataset /path/to/dataset_folder \
    --outdir /path/to/output
```

The model predictions (Contours visualization `PNG` and the instance mask `npy` will be saved)

### Output Files 

- `*_contours.png`: Original image with green contours overlaid on detected instances
- `*_contours.npy`: NumPy array containing the instance segmentation mask (0=background, 1,2,3...=instance labels)


## Example Run

We provide example PAS patches (512x512) in the [**examples**](../examples/) folder. 

<p align="left">
  <img src="../examples/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616.png" width="300">
</p>

1. Adjust the paths to your local setup. In the example below, we use the CellViT-256 (40×) backbone.


```bash
python /path/to/CellViT/cell_segmentation/inference/inference_cellvit_experiment_ca.py \
    --gpu 0 \
    --model /path/to/model_checkpoints/CellViT-256-x40-AMP.pth \
    --patching True \
    --overlap 0 \
    --dataset /path/to/stage1_paper/examples \
    --outdir /path/to/stage1_paper/cellvit-inference-gpu/result
```

2. Instance Segmentation Mask

<p align="left">
  <img src="result/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616_contours.png" width="300">
</p>


3. Binary/Semantic Mask 

The `*_contours.npy` instance mask can be converted to a binary mask by setting all non-zero (foreground) pixels to 1.


### mask to geojson 

For easy human-in-the-loop curation and correction, see [**mask_to_geojson_qupath.py**](../../mask_to_geojson_qupath.py).


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

@article{guo2024good,
  title={How Good Are We? Evaluating Cell AI Foundation Models in Kidney Pathology with Human-in-the-Loop Enrichment},
  author={Guo, Junlin and Lu, Siqi and Cui, Can and Deng, Ruining and Yao, Tianyuan and Tao, Zhewen and Lin, Yizhe and Lionts, Marilyn and Liu, Quan and Xiong, Juming and others},
  journal={arXiv preprint arXiv:2411.00078},
  year={2024}
}

@article{wang2025evaluating,
  title={Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models},
  author={Wang, Runchen and Guo, Junlin and Lu, Siqi and Deng, Ruining and Lu, Zhengyi and Zhu, Yanfan and Yang, Yuechen and Qu, Chongyu and Wang, Yu and Zhao, Shilin and others},
  journal={arXiv preprint arXiv:2510.01287},
  year={2025}
}
```