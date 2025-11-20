# Evaluating Cell AI Foundadtion Models (FMs) in Kidney Pathology with Human-in-the-Loop Enrichment

**TL;DR**: 

- Using multiple cell FMs to scalably enrich annotations and enable continuous improvement. Continuously built following large-scale evaluation (**stage 1**)

- This work benchmarks the evaluation (**stage 1**) and fine-tuning (**stage 2**) on Cellpose 2.0, StarDist (Histo.), and CellViT in kidney pathology. 

- **Keywords**: CellFM-HITL framework for assessment + efficient model refinement; Cell FMs

## CellFM-HITL Workflow 

1. Construct Large-scale, Diverse dataset for Evaluation

<p align="center">
  <img src="../assets/unexplored_dataset.png" width="800">
</p>


2. Less model bias and more generalizability — performing multiple cell FMs Inference and segmentaiton ratings.

<p align="center">
  <img src="../assets/performance_rating.png" width="770">
</p>


3. How can we efficiently improve them ? Our CellFM-HITL Data Enrichment.

<p align="center">
  <img src="../assets/performance_enhancement.png" width="800">
</p>