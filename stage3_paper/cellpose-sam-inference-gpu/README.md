# Run Cellpose-SAM for nuclei segmentation

- Run **Cellpose-SAM (Cellpose 4.0+)** for nuclei segmentation on a folder of images

- This script is adapted from the official Cellpose-SAM Colab notebook by Marius Pachitariu, Michael Rariden, and Carsen Stringer.
It supports batch processing of `.png` or `.tif` images using GPU acceleration.

## Setup 

Create a conda environment (e.g., cellpose-sam)
```bash
conda create -n cellpose-sam python=3.9
conda activate cellpose-sam
```

Install the required packages:
```
pip install git+https://github.com/mouseland/cellpose.git
pip install matplotlib tqdm numpy
```
## Usage:
    python run_cellpose_sam.py --input_dir /path/to/images --output_dir /path/to/output --ext .png

### Alternative: run_Cellpose_SAM.ipynb

## Exampe Run


We provide example PAS patches (512x512) in the [**examples**](../examples/) folder. 

<p align="left">
  <img src="../examples/2-WXA-FFS-PH-20220322-01(2)%20rat%20kindey%20PAS_patch_5120_47616.png" width="300">
</p>


Run the script
```bash
python run_cellpose_sam.py --input_dir /path/to/stage3_paper/examples --output_dir /path/to/stage3_paper/cellpose-sam-inference-gpu/result --ext .png
```


The results are saved in `png` (visualization) and `npy` format. 

- **`*_contours.png`**: Original image with green contours overlaid on detected instances
- **`*_contours.npy`**: NumPy array containing the instance segmentation mask (0=background, 1,2,3...=instance labels)

<p align="left">
  <img src="result/2-WXA-FFS-PH-20220322-01(2)%20rat%20kindey%20PAS_patch_5120_47616_contours.png" width="300">
</p>

### mask to geojson 

For easy human-in-the-loop curation and correction, see [**mask_to_geojson_qupath.py**](../../mask_to_geojson_qupath.py).


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