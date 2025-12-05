# CellViT Framework Fine-tuning and Models

## Installation 
<!-- The same conda environment used for training + inference as in [cellvit-inference-gpu](../../stage1_paper/cellvit-inference-gpu/README.md#installation). -->

### Option 1: Use Conda

```bash
conda env create -f environment.yml
conda activate <env_name>
```

### Option 2: Use Pip 

```bash
conda create -n <env_name> python=3.9.7
conda activate <env_name>

pip install -r requirements.txt
```
The [environment.yml](https://github.com/TIO-IKIM/CellViT/blob/main/environment.yml) and [requirements.txt](https://github.com/TIO-IKIM/CellViT/blob/main/requirements.txt) files are taken from the original CellViT [<ins>GitHub repo</ins>](https://github.com/TIO-IKIM/CellViT/tree/main) (link here). 


## Model Weights and Inference

## Training Instructions

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