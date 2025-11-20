# Inference Baselines 

This folder provides the customized patch-level inference baselines for the cell foundation models (FMs): Cellpose 2.0, StarDist(Histo.), and CellViT. 

## Overview
It is based on our stages 1 and 2 paper using cell FMs released before 2024 Aug.

- Stage-1 Performance Assessment: [Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology](https://arxiv.org/abs/2408.06381)
- Stage-2 A CellFM-HITL Framework for Assessment (Stage-1) and Efficient Enhancement: [Evaluating Cell AI Foundation Models in Kidney Pathology with Human-in-the-Loop Enrichment](https://arxiv.org/abs/2411.00078)

## Cell FMs Released Before 2024 Aug.

| Year–Month | Model                 | Backbone        | Post-processing       | Original Repo                                 | Model Paper                                                                                  | Custom Patch-Level Pipeline                         | Our Work                                                                                                               |
|-------------|----------------------|-----------------|-----------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| 2022 Mar   | **StarDist (Histo.)** | U-Net           | Star-convex Polygon   | [Link](https://github.com/stardist/stardist)  | [ISBI 2022](https://arxiv.org/abs/2203.02284)                                                | [StarDist Inference](stardist-inference-gpu) · [QuPath Plugin](stardist-inference-gpu/use-startdist-in-qupath) | [Medical Imaging 2025](https://arxiv.org/abs/2408.06381) (Stage 1); <br>[Nat. Commun. Med. 2025](https://arxiv.org/abs/2411.00078) (Stage 2)|
| 2022 Nov   | **Cellpose 2.0**          | U-Net           | GradientFlow Tracking | [Link](https://github.com/MouseLand/cellpose) | [Nat. Methods 2021](https://www.nature.com/articles/s41592-020-01018-x)                      | [Cellpose Inference](cellpose-inference-gpu)                      | (same as above)                                                                                                       |
| 2023 Oct   | **CellViT**           | ViT (HIPT, SAM) | HoVer-Net             | [Link](https://github.com/TIO-IKIM/CellViT)   | [Med. Image Anal. 2023](https://www.sciencedirect.com/science/article/pii/S1361841524000689) | [CellViT Inference](cellvit-inference-gpu)                       | (same as above)                                                                                                       |
## Our Direct Usage of Multiple Cell FMs for Inference in CellFM-HITL

1. Large-scale, Diverse dataset for Evaluation 

<p align="center">
  <img src="../assets/unexplored_dataset.png" width="800">
</p>


2. Less model bias and more generalizability — leveraging multiple cell FMs!

<p align="center">
  <img src="../assets/performance_rating.png" width="770">
</p>

