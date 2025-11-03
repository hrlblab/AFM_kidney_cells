# CellFM-HITL: A Multi-Foundation-Model–Based Human-in-the-Loop Framework for Efficient Data Enrichment and Model Evaluation in Nuclei Segmentation

>**TL;DR**: We provide and continuously update class-agnostic **Cell AI foundation model (FMs)** inference and fine-tuning codebases for nuclei instance segmentation in histopathology, along with a **Human-in-the-Loop (HITL)** framework that unifies multiple Cell FMs. The framework also efficiently combines **model pedictions with minimal expert annotation** on challenging cases to **enhance performance** and streamline pathology workflows.


## 📢 Latest Updates
An ongoing project updating new cell foundation models, evaluations, and nuclei segmentation performance (demonstrated on kidney pathology).

🔥 🔥 🔥 Last Updated on 2025.11.3 🔥 🔥 🔥
- **[2025.10.30]** Our latest paper [*“Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models”*](https://arxiv.org/abs/2510.01287) has been accepted for **Medical Imaging 2026** *(New FMs assessment — Cell FMs released by 2025 Aug.)*  
- **[2025.10.14]** Our journal paper [*“Evaluating Cell AI Foundation Models in Kidney Pathology with Human-in-the-Loop Enrichment”*](https://arxiv.org/abs/2411.00078) has been accepted for **Nature Communications Medicine** *(Data-efficient CellFMs-HITL framework — demonstrated in kidney pathology on Cell FMs released by 2024 Aug.)*  
- **[2024.10.27]** Our first paper [*“Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology”*](https://arxiv.org/abs/2408.06381) has been accepted for **Medical Imaging 2025** *(First large-scale FMs assessment in Kidney Pathology— Cell FMs released by 2024 Aug.)*

> 🧩 Annotation preparation for the **2nd KPI Challenge** is currently in progress.

## 🎯 Highlights

- **Perform SOTA Cell AI FMs Assessment:**  Ready-to-use patch-level inference pipelines for evaluating cell nuclei instance segmentation.

- **Multi-FMs-based HITL Data Enrichment Framework:**  Scalably enriches high-quality labeled nuclei image patches with cell FMs, boosting model performance while reducing expert annotation effort.

- **Cell AI FMs Fine-tuning Support:**  Includes patch-level fine-tuning codebases for domain-specific model enhancement (e.g., kidney pathology).
  
## 🚀 CellFM-HITL Workflow
- Step 1: **Individual Cell FMs Performance** ([Cell FMs Inference Pipeline & Model Summary](#-cell-fms-inference-pipeline--model-summary)).

- Step 2: **Multi-FMs Performance Rating and Data Enrichment** ([CellFMs-HITL Data Enrichment Illustration](#%EF%B8%8F-cellfms-hitl-data-enrichment-illustration)).  

- Step 3: **Cell FMs Continuous Fine-Tuning with Scalably Enriched Data** ([Continuous Model Fine-Tuning with Enriched Data](#-continuous-model-fine-tuning-with-enriched-data)).  


## 🔬 Cell FMs Inference Pipeline & Model Summary
We detail the evaluated SOTA cell FMs, their architectures, post-processing methods, original sources, and our custom patch-level inference pipeline codes.

### Cell FMs Released Before 2024 Aug.

| Year–Month | Model                 | Backbone        | Post-processing       | Original Repo                                 | Model Paper                                                                                  | Custom Patch-Level Pipeline                         | Our Work                                                                                                               |
|-------------|----------------------|-----------------|-----------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 2022 Mar   | **StarDist (Histo.)** | U-Net           | Star-convex Polygon   | [Link](https://github.com/stardist/stardist)  | [ISBI 2022](https://arxiv.org/abs/2203.02284)                                                | [StarDist Inference](#) · [QuPath Plugin](#) | [Medical Imaging 2025](https://arxiv.org/abs/2408.06381); <br>[Nat. Commun. Med. 2025](https://arxiv.org/abs/2411.00078) |
| 2022 Nov   | **Cellpose**          | U-Net           | GradientFlow Tracking | [Link](https://github.com/MouseLand/cellpose) | [Nat. Methods 2021](https://www.nature.com/articles/s41592-020-01018-x)                      | [Cellpose Inference](#)                      | (same as above)                                                                                                       |
| 2023 Oct   | **CellViT**           | ViT (HIPT, SAM) | HoVer-Net             | [Link](https://github.com/TIO-IKIM/CellViT)   | [Med. Image Anal. 2023](https://www.sciencedirect.com/science/article/pii/S1361841524000689) | [CellViT Inference](#)                       | (same as above)                                                                                                       |




### Cell FMs Released 2024 Aug. – 2025 Aug.

| Year–Month | Model | Backbone | Post-processing | Original Repo | Model Paper | Custom Patch-Level Inference | Our Work |
|-------------|--------|----------------------|-----------------|----------------|--------------|----------------------------------|------------------|
| 2025 Jan | **CellViT++** | ViT (HIPT, SAM, Virchow, UNI) | HoVer-Net | [Link](https://github.com/TIO-IKIM/CellViT-Plus-Plus) | [arXiv](https://arxiv.org/abs/2501.05269) | [CellViT++ Patch Inference (updating)](#) | [Medical Imaging 2026](https://arxiv.org/abs/2510.01287)|
| 2025 May | **Cellpose-SAM** | SAM | GradientFlow Tracking | [Link](https://github.com/MouseLand/cellpose) | [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.04.28.651001v1) | [Cellpose-SAM Inference (updating)](#) | [Medical Imaging 2026](https://arxiv.org/abs/2510.01287)|


## ⚙️ CellFMs-HITL Data Enrichment Illustration



## 🔁 Continuous Model Fine-Tuning with Enriched Data

Provides python codesfor patch-level cell FMs fine-tuning to improve model performance in domain-specific datasets (e.g., kidney pathology).

## Results 
- updating arXiv figures and results with final versions 

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
