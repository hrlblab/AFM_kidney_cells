# StarDist GPU Inference
A patch-level GPU inference code using the StarDist (Histo.). This script processes directories of PNG images and performs instance or binary segmentation with configurable parameters. The main script is `stardist_gpu.py`.

## Requirements

### System

- Python 3.8 and TensorFlow 2.4 (the version we use)
- CUDA-compatible GPU (recommended) or CPU
- NVIDIA GPU drivers (for GPU support)

### Installation 

### Option 1: Step-by-Step Install 


1. Create the conda environment from the `csbdeep` TF 2.4 YAML (you can rename the env in the file): see the [installation guide](https://github.com/CSBDeep/CSBDeep/tree/main/extras#conda-environment).

    ```bash
    conda env create -f https://raw.githubusercontent.com/CSBDeep/CSBDeep/main/extras/environment-gpu-py3.8-tf2.4.yml
    ```
2. StarDist can then be installed with `pip`:

    TensorFlow 2 (version 2.x.x): 
    ```bash
    pip install stardist
    ```
3. Other packages/libraries such as `numpy`, `pillow`, `cv2`. Check that `numpy==1.19.5`. Exact versions are listed in [requirements.txt](requirements.txt) (or [environment.yml](environment.yml)).

### Option 2: Use environment.yml / requirements.txt

- use conda: 

    ```bash
    conda env create -f environment.yml
    conda activate <env_name>
    ```

- use pip 
    ```bash
    conda create -n <env_name> python=3.8
    conda activate <env_name>

    pip install -r requirements.txt
    ```

## Usage

### 1. Configure Input and Output Paths

```python
# Path to image directory
image_dir = '/path/to/your/images'
image_files = glob.glob(os.path.join(image_dir, '*.png'))

# Output directory
output_dir = '/path/to/output'
os.makedirs(output_dir, exist_ok=True)
```
### 2. Run the Script

Execute the script by running:

```bash
python stardist_inference.py
```

### 3. Output Mode 

In `stardist_gpu.py`, the output mode is controlled by the `BINARY` flag:

```python
# Instance segmentation output (default)
BINARY = False  

# Binary mask output
BINARY = True
```
#### Instance Segmentation Mode (Default)

- **`*_contours.png`**: Original image with green contours overlaid on detected instances
- **`*_contours.npy`**: NumPy array containing the instance segmentation mask (0=background, 1,2,3...=instance labels)

#### Binary Segmentation Mode (`BINARY=True`)

- **`*_grayscale.png`**: Binary mask saved as grayscale image (white=cell, black=background)




### 4. Customizing Inference Parameters

You can customize the inference by modifying the following parameters in the script:
- **`model_type`**: The type of StarDist2D model to use (default is `"2D_versatile_he"`).
- **`use_gpu`**: Set to `True` to enable GPU usage if available.
- **`nms_thresh`**: Non-Maximum Suppression threshold (optional).
- **`prob_thresh`**: Probability threshold for object detection (optional).


## Example Run
We provide example PAS patches (512x512) in the [**examples**](../examples/) folder. 

<p align="left">
  <img src="../examples/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616.png" width="300">
</p>

1. Paths and Output Dir:
```python
# Path to image directory
image_dir = '/path/to/stage1_paper/examples'
image_files = glob.glob(os.path.join(image_dir, '*.png'))

# Output directory
output_dir = '/path/to/stage1_paper/stardist-inference-gpu/result'
os.makedirs(output_dir, exist_ok=True)
```
2. Run the script
```bash
python stardist_gpu.py
```
3a. Instance Segmentation (Default)
<p align="left">
  <img src="result/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616_contours.png" width="300">
</p>


3b. Binary Segmentation (if `BINARY=True`)
<p align="left">
  <img src="result/2-WXA-FFS-PH-20220322-01(2) rat kindey PAS_patch_5120_47616_grayscale.png" width="300">
</p>


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