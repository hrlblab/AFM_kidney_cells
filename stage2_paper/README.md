# Evaluating Cell AI Foundadtion Models (FMs) in Kidney Pathology with Human-in-the-Loop Enrichment

**TL;DR**: 

- Using multiple cell FMs to scalably enrich annotations and for continuous model improvement.

- Benchmarking performance evaluation (**stage 1**) and fine-tuning (**stage 2**) on Cellpose 2.0, StarDist (Histo.), and CellViT in kidney pathology. 

- Can be adapted for Newer models (**stage 3**).


## Overview 

- Stage-1 Performance Assessment: [**Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology**](https://arxiv.org/abs/2408.06381)
- Stage-2 A CellFM-HITL Framework for Assessment (Stage-1) and Efficient Enhancement: [**Evaluating Cell AI Foundation Models in Kidney Pathology with Human-in-the-Loop Enrichment**](https://arxiv.org/abs/2411.00078)




## CellFM-HITL Workflow 

1. Construct Large-scale, Diverse dataset for Evaluation.

<p align="center">
  <img src="../assets/unexplored_dataset.png" width="800">
</p>


2. Less model bias and more generalizability — performing multiple cell FMs Inference and segmentaiton ratings.

<p align="center">
  <img src="../assets/performance_rating.png" width="770">
</p>




3. How can we efficiently improve FMs for Kidney ? Our CellFM-HITL Data Enrichment.

<!-- <p align="center">
  <img src="../assets/performance_enhancement.png" width="800">
</p> -->


<p align="center">
  <img src="../assets/HITL-pipelines.png" width="800">
</p>

This work have experimented the following annotation enrichment strategies for model finetuning. 

  - **Easy patches**: Foundation model-generated pseudo labels.
  - **Hard patches**: Pathologist-corrected shared failure cases
  - **Combined set**: Combination of easy and hard patches for balanced refinement.


## Implementations

### 1. Individual Cell FMs Inference and Ratings

| Year–Month | Model | Backbone | Post-processing  | Inference code|
|:---:|:---:|:---:|:---:|:---:|
| 2022 Mar | StarDist (Histo.) | U-Net | Star-convex Polygon |[StarDist Inference](../stage1_paper/stardist-inference-gpu/README.md)|
| 2022 Nov | Cellpose 2.0 | U-Net |GradientFlow Tracking |[Cellpose 2.0 Inference](../stage1_paper/cellpose-inference-gpu/README.md) |
| 2023 Oct | CellViT  | ViT (HIPT, SAM) |HoVer-Net |[CellViT Inference](../stage1_paper/cellvit-inference-gpu/README.md)|


- Since Stage 2 focused on validating the CellFM-HITL framework, the FMs evaluated were released before August 2024.

- We also have the new cell FMs (**Cellpose-SAM, CellViT++ variants released 2024 Aug. - 2025 Aug.**) assessment, in [**stage3_paper folder**](../stage3_paper/).

### 2. Data/Annotations Enrichment with FMs 

 
- Python script for converting prediction to geojson (in **QuPath**) is provided, [**mask_to_geojson_qupath.py**](../mask_to_geojson_qupath.py).

### 3. Continously Finetuned with Enriched data 


- We also experimented each annotation enrichment strategy with different dataset scales (25%, 50% ... 100%)

<p align="left">
  <img src="../assets/experiment_table.png" width="800">
</p>



#### Access/Use Finetuned Models 



#### Model Finetuning Codebases 

See `[model name]_kidney_finetune` directories in this folder. 

## Results 

<p align="left">
  <a href='https://arxiv.org/abs/2411.00078'><img src='https://img.shields.io/badge/Stage2--Paper-Nat.Comm.Med.-red'></a> 
</p>

### Model Performances 

<p align="center">
  <img src="../assets/performance_rating_results.png" width="800">
</p>

### Performance after Finetuning 

- Baselines: We evaluated each foundation model’s (Cellpose, StarDist, CellViT) pre-trained weights on our hold-out test set.

- F1-score comparisons across training/annotation strategies are shown (below). Full metrics (F1, Precision, Recall) are provided in the [Table](../assets/f1-recall-prec.png).

<br>

<p align="center">
  <img src="../assets/results-f1.png" width="800">
</p>


- Qualitative results. Areas of improvement highlighted by rectangles.

<p align="center">
  <img src="../assets/qualitative.png" width="600">
</p>

#### Observation 

- **Baseline performance evaluation**, CellViT achieves the highest F1 score of 0.78. Kidney-targeted FMs still required.
- **Fine-tuning with enriched data** improves all three models, with StarDist achieving the highest F1 score of 0.82. 
- **Annotation Enrichment**: We found the **combination** of the <ins>foundation model–generated pseudo-labels</ins> and <ins>a subset of pathologist-corrected hard patches</ins> yields consistent performance gains across all models.

 ### This CellFM-HITL Assessment and Enhancement Framework can be Iterative.

<p align="left">
  <a href='https://arxiv.org/abs/2510.01287'><img src='https://img.shields.io/badge/Stage3--Paper-SPIE-26'></a> 
</p>


- With newer Cell AI FMs (2025) such as CellViT++[Virchow] and Cellpose-SAM, a portion of the **previously rated “medium” or challenging patches** are now correctly labeled by these newer models (rated as “Good”). 


<br>

<p align="center">
  <img src="../assets/stage3_performance_rating.png" width="500">
</p>