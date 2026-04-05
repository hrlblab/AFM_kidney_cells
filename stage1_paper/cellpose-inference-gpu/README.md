# Cellpose GPU Inference

A customized patch-level GPU inference code using the **Cellpose 2.0** model. This script processes directories of PNG images and performs instance or binary segmentation with configurable parameters.


## Requirements

### System Requirements

- Python 3.9 or higher (we use 3.9)
- CUDA-compatible GPU (recommended) or CPU
- NVIDIA GPU drivers (for GPU support)

## Installation

Ensure successful loading packages/librareis of `cellpose_gpu.py`. Detail versions like `cellpose` (for baseline inference, CNN based backbone in this paper is `cellpose 2.0+`, the SAM ViT-H based backbone is `cellpose 4.0+` in [Stage 3 Paper](../../stage3_paper/cellpose-sam-inference-gpu/)), etc can be found in `environment.yml` or `requirements.txt`

### Option 1: Using Conda (Recommended)

Create a conda environment from the provided `environment.yml`:

```bash
conda env create -f environment.yml
conda activate <env_name>
```

### Option 2: Using pip (Recommended)

Install the required packages:

```bash
conda create -n <env_name> python=3.9
conda activate <env_name> 

pip install numpy cellpose pillow opencv-python
```

**Note**: For GPU support, you'll also need PyTorch with CUDA. Install PyTorch separately based on your CUDA version:

```bash
# Example for CUDA 11.3
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu113
```

### Option 3: Install from requirements.txt

```bash
conda create -n <env_name> python=3.9
conda activate <env_name> 

pip install -r requirements.txt
```

## Usage

### Basic Usage

1. **Configure Input and Output Paths** (`cellpose_gpu.py`):

```python
# Path to image directory
image_dir = '/path/to/your/images'
image_files = glob.glob(os.path.join(image_dir, '*.png'))

# Output directory
output_dir = '/path/to/output'
os.makedirs(output_dir, exist_ok=True)
```

2. **Run the script**:

```bash
python cellpose_gpu.py
```

### Programmatic Usage

You can also use the `CellposeProcessor` class in your own code:

```python
from cellpose_gpu import CellposeProcessor
import glob
import os

# Initialize the processor
cellpose_model = CellposeProcessor(use_gpu=True, model_type="nuclei")

# Get image files
image_files = glob.glob(os.path.join(image_dir, '*.png'))

# Run inference
cellpose_model.inference_instance_loop(
    image_files=image_files,
    output_dir=output_dir,
    flow_threshold=0.8,
    min_size=15,
    binary=False
)
```


### Output Files

#### Instance Segmentation Mode (`binary=False`)

- **`*_contours.png`**: Original image with green contours overlaid on detected instances
- **`*_contours.npy`**: NumPy array containing the instance segmentation mask (0=background, 1,2,3...=instance labels)

#### Binary Segmentation Mode (`binary=True`)

- **`*_grayscale.png`**: Binary mask saved as grayscale image (white=cell, black=background)

### Example Run

We provide example PAS patches (512x512) in the [**examples**](../examples/) folder. 

<p align="left">
  <img src="../examples/2-WXA-FFS-PH-20220322-01(2)%20rat%20kindey%20PAS_patch_5120_47616.png" width="300">
</p>

1. Paths and Output Dir:
```python
# Path to image directory
image_dir = '/path/to/stage1_paper/examples'
image_files = glob.glob(os.path.join(image_dir, '*.png'))

# Output directory
output_dir = '/path/to/stage1_paper/cellpose-inference-gpu/result'
os.makedirs(output_dir, exist_ok=True)
```
2. Run the script
```bash
python cellpose_gpu.py
```

3a. Instance Segmentation (Default)
<p align="left">
  <img src="result/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616_contours.png" width="300">
</p>


3b. Binary Segmentation (if `binary=True`)
<p align="left">
  <img src="result/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616_grayscale.png" width="300">
</p>

### mask to geojson 

For easy human-in-the-loop curation and correction, see [**mask_to_geojson_qupath.py**](../../mask_to_geojson_qupath.py).




## Parameters

### CellposeProcessor Initialization

- `use_gpu` (bool): Enable GPU acceleration (default: `True`)
- `model_type` (str): Cellpose model type, e.g., `"nuclei"` or `"cyto"` (default: `"nuclei"`)

### inference_instance_loop Parameters

- `image_files` (list): List of paths to PNG image files
- `output_dir` (str): Directory where results will be saved
- `binary` (bool): If `True`, saves binary masks; if `False`, saves instance segmentation with contours (default: `False`)
- `flow_threshold` (float): Maximum allowed error of flows for each mask (default: `0.4`)
  - Lower values = stricter mask quality
  - we use `0.8` for our kidney cell datasets for better results.
- `min_size` (int): Minimum number of pixels per mask (default: `15`)
  - Set to `-1` to disable minimum size filtering



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