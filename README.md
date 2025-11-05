# CellFM-HITL: A Multi-Foundation-Model–Based Human-in-the-Loop Framework for Efficient Data Enrichment and Model Evaluation in Nuclei Segmentation

>**TL;DR**: We continuously **provide/update** patch-level class-agnostic **Cell AI foundation model (FMs)** inference and fine-tuning codebases for nuclei instance segmentation in histopathology, along with a **Human-in-the-Loop (HITL)** framework that unifies multiple Cell FMs. The framework also efficiently combines **model pedictions with minimal expert annotation** on challenging cases to **enhance performance** and streamline pathology workflows.

<p align="center">
  <a href='https://arxiv.org/abs/2408.06381'><img src='https://img.shields.io/badge/Stage1--Paper-SPIE-25'></a> 
  <a href='https://arxiv.org/abs/2411.00078'><img src='https://img.shields.io/badge/Stage2--Paper-Nat.Comm.Med.-red'></a> 
  <a href='https://arxiv.org/abs/2510.01287'><img src='https://img.shields.io/badge/Stage3--Paper-SPIE-26'></a> 
</p>

<p align="center">
  <a href="#-latest-updates">Latest Updates</a> •
  <a href="#-highlights">Highlights</a> •
  <a href="#-cellfm-hitl-workflow-overview">Workflow</a> •
  <a href="#-cell-fms-inference-pipeline--model-summary">Model Summary</a> •
  <a href="#%EF%B8%8F-cellfms-hitl-data-enrichment-illustration">Data Enrichment</a> •
  <a href="#-continuous-model-fine-tuning-with-enriched-data">Fine-Tuning</a> •
  <a href="#results">Results</a> •
  <a href="#citation">Citation</a> •
  <a href="#awesome-histopathological-nuclei-segmentation-models">Awesome Cell FMs List</a>
</p>



## 📢 Latest Updates
This **ongoing project** welcomes researchers to **share** their work with the **cell segmentation community** by submitting pull requests or issues to add or update paper information here: [**Awesome Histopathological Nuclei Segmentation Models**](#awesome-histopathological-nuclei-segmentation-models).


🔥 🔥 🔥 Last Updated on 2025.11.5 🔥 🔥 🔥
- **[2025.10.30]** (**Stage 3 Conf. Paper**) **[*“Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models”*](https://arxiv.org/abs/2510.01287)** has been accepted for **Medical Imaging 2026** *(New FMs assessment — Cell FMs released by 2025 Aug.)*  
- **[2025.10.14]** (**Stage 2 Journal Paper**) **[*“Evaluating Cell AI Foundation Models in Kidney Pathology with Human-in-the-Loop Enrichment”*](https://arxiv.org/abs/2411.00078)** has been accepted for **Nature Communications Medicine 2025** *(Data-efficient CellFMs-HITL framework — demonstrated in kidney pathology on Cell FMs released by 2024 Aug.)*  
- **[2024.10.27]** (**Stage 1 Conf. Paper**) **[*“Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology”*](https://arxiv.org/abs/2408.06381)** has been accepted for **Medical Imaging 2025** *(First large-scale FMs assessment in Kidney Pathology— Cell FMs released by 2024 Aug.)*

> 🧩 Annotate/Curated Dataset preparation for the **2nd KPI Challenge** is currently in progress.

## 🎯 Highlights

- **Perform SOTA Cell AI FMs Assessment:**  Ready-to-use patch-level instance segmentation inference pipelines.

- **Multi-FMs-based HITL Data Enrichment Framework:**  Scalably enriches high-quality labeled nuclei image patches with cell FMs, boosting performance while reducing expert annotation effort.

- **Cell AI FMs Fine-tuning Support:**  Patch-level fine-tuning codebases for continous model enhancement.
  
## 🚀 CellFM-HITL Workflow Overview

- Step 1: **Individual Current SOTA Cell FMs Performance** ([Cell FMs Inference Pipeline & Model Summary](#-cell-fms-inference-pipeline--model-summary)) (Stages 1, 2, 3 Papers)

- Step 2: **Multi-FMs Performance Rating and Data Enrichment** ([CellFMs-HITL Data Enrichment Illustration](#%EF%B8%8F-cellfms-hitl-data-enrichment-illustration)) (Stage 2 Paper)

- Step 3: **Cell FMs Continuous Fine-Tuning with Scalably Enriched Data** ([Continuous Model Fine-Tuning with Enriched Data](#-continuous-model-fine-tuning-with-enriched-data)) (Stage 2 Paper)


## 🔬 Cell FMs Inference Pipeline & Model Summary

The tables summarize the evaluated SOTA cell FMs, their code sources, and our custom patch-level inference Python pipelines from our Stages 1, 2, 3 papers' model assessments.

### Cell FMs Released Before 2024 Aug.

| Year–Month | Model                 | Backbone        | Post-processing       | Original Repo                                 | Model Paper                                                                                  | Custom Patch-Level Pipeline                         | Our Work                                                                                                               |
|-------------|----------------------|-----------------|-----------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 2022 Mar   | **StarDist (Histo.)** | U-Net           | Star-convex Polygon   | [Link](https://github.com/stardist/stardist)  | [ISBI 2022](https://arxiv.org/abs/2203.02284)                                                | [StarDist Inference](stage1_paper/stardist-inference-gpu) · [QuPath Plugin](stage1_paper/stardist-inference-gpu/use-startdist-in-qupath) | [Medical Imaging 2025](https://arxiv.org/abs/2408.06381) (Stage 1); <br>[Nat. Commun. Med. 2025](https://arxiv.org/abs/2411.00078) (Stage 2)|
| 2022 Nov   | **Cellpose**          | U-Net           | GradientFlow Tracking | [Link](https://github.com/MouseLand/cellpose) | [Nat. Methods 2021](https://www.nature.com/articles/s41592-020-01018-x)                      | [Cellpose Inference](stage1_paper/cellpose-inference-gpu)                      | (same as above)                                                                                                       |
| 2023 Oct   | **CellViT**           | ViT (HIPT, SAM) | HoVer-Net             | [Link](https://github.com/TIO-IKIM/CellViT)   | [Med. Image Anal. 2023](https://www.sciencedirect.com/science/article/pii/S1361841524000689) | [CellViT Inference](stage1_paper/cellvit-inference-gpu)                       | (same as above)                                                                                                       |




### Cell FMs Released 2024 Aug. – 2025 Aug.

| Year–Month | Model | Backbone | Post-processing | Original Repo | Model Paper | Custom Patch-Level Inference | Our Work |
|-------------|--------|----------------------|-----------------|----------------|--------------|----------------------------------|------------------|
| 2025 Jan | **CellViT++** | ViT (HIPT, SAM, Virchow, UNI) | HoVer-Net | [Link](https://github.com/TIO-IKIM/CellViT-Plus-Plus) | [arXiv](https://arxiv.org/abs/2501.05269) | [CellViT++ Patch Inference (updating)](stage3_paper/cellvit-plusplus-inference-gpu) | [Medical Imaging 2026](https://arxiv.org/abs/2510.01287) (Stage 3)|
| 2025 May | **Cellpose-SAM** | SAM | GradientFlow Tracking | [Link](https://github.com/MouseLand/cellpose) | [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.04.28.651001v1) | [Cellpose-SAM Inference (updating)](stage3_paper/cellpose-sam-inference-gpu) | [Medical Imaging 2026](https://arxiv.org/abs/2510.01287) (Stage 3)|

<br>

🔥 **Notes**:
Awesome histopathological nuclei segmentation FMs or Specialists are continuously updated here: [**Awesome Histopathological Nuclei Segmentation Models**](#awesome-histopathological-nuclei-segmentation-models).



## ⚙️ CellFMs-HITL Data Enrichment Illustration

**Motivation**: There is still limited understanding of AI/DL models’ performance in nuclei segmentation on complex organs (e.g., kidney). **How good are we? How can we improve it scalably?** 

1. Large-scale, Diverse dataset for Evaluation 

<p align="center">
  <img src="assets/unexplored_dataset.png" width="800">
</p>


2. Less model bias and more generalizability — leveraging multiple cell FMs!

<p align="center">
  <img src="assets/performance_rating.png" width="770">
</p>


3. How can we efficiently improve them ? Our CellFM-HITL Data Enrichment.

<p align="center">
  <img src="assets/performance_enhancement.png" width="800">
</p>

4. This HITL framework can be iterative. See advances of CellFMs in our Stage 3 paper.
<p align="center">
  <img src="assets/stage3_performance.png" width="800">
</p>


## 🔁 Continuous Model Fine-Tuning with Enriched Data

We currently provide fine-tuning codebases and models for our Stage 2 paper using Cell FMs released before Aug 2024 (Cellpose, StarDist, CellViT). Patch-level fine-tuning support for newer Cell FMs will be added as part of our upcoming Stage 3 work.



## Results 

<p align="left">
  <a href='https://arxiv.org/abs/2411.00078'><img src='https://img.shields.io/badge/Stage2--Paper-Nat.Comm.Med.-red'></a> 
</p>

### Model Performances 

- Individual model predictions (**Cellpose, StarDist, CellViT**) are rated.

- **Shared failure cases** across all models highlight **domain gaps in kidney pathology** and important for targeted fine-tuning.

- Fusing the **"Good"** predictions from multiple FMs **enriches the labeled dataset** with less single-model bias and better generalization.

<p align="center">
  <img src="assets/performance_rating_results.png" width="800">
</p>

### Data Enrichement

Our enriched labeled dataset comes from:

- **Easy patches:** Foundation model-generated pseudo labels.
- **Hard patches:** Pathologist-corrected shared failure cases
- **Combined set:** Combination of easy and hard patches for balanced refinement.

<br>

![](assets/experiments-settings.png)

### CellFM-HTML Performance Validation

- Baselines: We evaluated each foundation model’s (Cellpose, StarDist, CellViT) pre-trained weights on our hold-out test set.

- F1-score comparisons across training/annotation strategies are shown (below). Full metrics (F1, Precision, Recall) are provided in the [Table](assets/f1-recall-prec.png).

<br>

<p align="center">
  <img src="assets/results-f1.png" width="800">
</p>



- Qualitative results. Areas of improvement highlighted by rectangles.

<p align="center">
  <img src="assets/qualitative.png" width="600">
</p>


 ### This CellFM-HITL Assessment and Enhancement Framework can be Iterative.
<p align="left">
  <a href='https://arxiv.org/abs/2510.01287'><img src='https://img.shields.io/badge/Stage3--Paper-SPIE-26'></a> 
</p>







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

## Awesome Histopathological Nuclei Segmentation Models

New awesome histopathological nuclei segmentation FMs or Specialists are continuously updated in this section. 
