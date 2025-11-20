# Evaluating Cell AI Foundadtion Models (FMs) in Kidney Pathology with Human-in-the-Loop Enrichment

**TL;DR**: 

- Using multiple cell FMs to scalably enrich annotations and enable continuous improvement. Continuously built following large-scale evaluation (**stage 1**).

- This work benchmarks the evaluation (**stage 1**) and fine-tuning (**stage 2**) on Cellpose 2.0, StarDist (Histo.), and CellViT in kidney pathology. 


## Overview 
It is based on our stages 1 and 2 paper using cell FMs released before 2024 Aug.

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


## Implementations and Code

### 1. Individual Cell FMs Inference and Ratings

- Python scripts to run patch-level inference on the pretrained cell FMs (**Cellpose 2.0, StarDist, and CellViT**) can be found in [**stage1_paper folder**](../stage1_paper/README.md#cell-fms-released-before-2024-aug). 

- Example of the *Rating Criteria* is provided in figure above. 

- Since stage 2 focused on validating the CellFM-HITL framework, foundation models evaluated were released before 2024 Aug. We also have the new cell FMs (**Cellpose-SAM, CellViT++ variants released 2024 Aug. - 2025 Aug.**) assessment, in [**stage3_paper folder**](../stage3_paper/).

### 2. Annotations/Curations on "Hard" patches in Qupath 

- After performance ratings on each FM predictions. We combined **"Easy"** (FMs-generated-pedictions) with **"Hard"** image patches for model refinement. These **"Hard"** image patches are corrected/annotated in Qupath. 

- Python script here for converting model predictions to geojson used in digital tools like Qupath are provided, [**mask_to_geojson_qupath.py**](../mask_to_geojson_qupath.py).