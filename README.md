# CellFM-HITL: A Multi-Foundation-Model–Based Human-in-the-Loop Framework for Efficient Data Enrichment and Model Evaluation in Nuclei Segmentation

>**TL;DR**: A human-in-the-loop (HITL) framework that integrates **multiple cell foundation models** (FMs) for nuclei instance segmentation, efficiently combining **model pedictions with minimal expert annotation** on challenging cases to **enhance performance** and streamline pathology workflows.

## 📢 Latest Updates
🔥 🔥 🔥 Last Updated on 2025.11.1 🔥 🔥 🔥
- **[2025.10.30]** Our latest paper [*“Evaluating New AI Cell Foundation Models on Challenging Kidney Pathology Cases Unaddressed by Previous Foundation Models”*](https://arxiv.org/abs/2510.01287) has been accepted for **Medical Imaging 2026** *(New FMs assessment — Cell FMs released by 2025 Aug.)*  
- **[2025.10.14]** Our journal paper [*“Evaluating Cell AI Foundation Models in Kidney Pathology with Human-in-the-Loop Enrichment”*](https://arxiv.org/abs/2411.00078) has been accepted for **Nature Communications Medicine** *(Data-efficient CellFMs-HITL framework — demonstrated in kidney pathology on Cell FMs released by 2024 Aug.)*  
- **[2024.10.27]** Our first paper [*“Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology”*](https://arxiv.org/abs/2408.06381) has been accepted for **Medical Imaging 2025** *(First large-scale Cell FMs assessment in Kidney Pathology— Cell FMs released by 2024 Aug.)*

> 🧩 Annotation preparation for the **2nd KPI Challenge** is currently in progress.

## 🎯 Highlights

- **Perform SOTA Cell AI FMs Assessment:**  Ready-to-use patch-level inference pipelines for evaluating cell nuclei instance segmentation.

- **Multi-FMs-based HITL Data Enrichment Framework:**  Scalably enriches high-quality labeled nuclei image patches with cell FMs, boosting model performance while reducing expert annotation effort.

- **Cell AI FMs Fine-tuning Support:**  Includes patch-level fine-tuning scripts for domain-specific model enhancement (e.g., kidney pathology).
  
## 🚀 CellFM-HITL Workflow
- Step 1: **Individual Cell FMs Performance** ([Cell FMs Inference Pipeline & Model Summary](#-inference-pipeline-model-summary)) 

- Step 2: **Multi-FMs Performance Rating and Data Enrichment** ([CellFMs-HITL Data Enrichment Illustration](#))  

- Step 3: **Cell FMs Continuous Fine-Tuning with Scalably Enriched Data** ([Continuous Model Fine-Tuning with Enriched Data](#))  


## 🔬 Cell FMs Inference Pipeline & Model Summary
We detail the evaluated SOTA cell FMs, their architectures, post-processing methods, original sources, and our customized patch-level inference pipeline.

### Cell FMs Released Before 2024 Aug.

| Year–Month | Model | Backbone | Post-processing | Original Repo | Model Paper | Patch-Level Pipeline | Our Work |
|-------------|--------|-----------|-----------------|----------------|--------------|----------------------|------------------|
| 2022 Mar | **StarDist (Histo.)** | U-Net | Star-convex Polygon | [Link](#) | [ISBI 2022](#) | [StarDist Inference](#) · [QuPath Plugin](#) | [Medical Imaging 2025](#)<br>[Nature Communications Medicine 2025](#) |
| 2022 Nov | **Cellpose** | U-Net | GradientFlow Tracking | [Link](#) | [Nature Methods 2021](#) | [Cellpose Inference](#) | [Medical Imaging 2025](#)<br>[Nature Communications Medicine 2025](#) |
| 2023 Oct | **CellViT** | ViT (HIPT, SAM) | HoVer-Net | [Link](#) | [Medical Image Analysis 2023](#) | [CellViT Inference](#) | [Medical Imaging 2025](#)<br>[Nature Communications Medicine 2025](#) |


### Cell FMs Released 2024 Aug. – 2025 Aug.

| Year–Month | Model | Backbone | Post-processing | Original Repo | Model Paper | Custom Patch-Level Inference | Our Work |
|-------------|--------|----------------------|-----------------|----------------|--------------|----------------------------------|------------------|
| 2025 Jan | **CellViT++** | ViT (HIPT, SAM, Virchow, UNI) | Star-convex Polygon | [Link](#) | [arXiv](#) | [CellViT++ Patch Inference](#) | [Medical Imaging 2026](#)|
| 2025 May | **Cellpose-SAM** | SAM | GradientFlow Tracking | [Link](#) | [bioRxiv](#) | [Cellpose-SAM Inference](#) | [Medical Imaging 2026](#)|


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
