# Evaluating Cell AI Foundadtion Models (FMs) in Kidney Pathology with Human-in-the-Loop Enrichment

<!-- ## Overview  -->

<!-- - Stage-1 Performance Assessment: [**Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology**](https://arxiv.org/abs/2408.06381)
- Stage-2 A CellFM-HITL Framework for Assessment (Stage-1) and Efficient Enhancement: [**Evaluating Cell AI Foundation Models in Kidney Pathology with Human-in-the-Loop Enrichment**](https://arxiv.org/abs/2411.00078) -->


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

This work have experimented the following **annotation enrichment strategies** for model finetuning. 

  - **Easy patches**: Foundation model-generated pseudo labels.
  - **Hard patches**: Pathologist-corrected shared failure cases
  - **Combined set**: Combination of easy and hard patches for balanced refinement.


## Results 

<p align="left">
  <a href='https://arxiv.org/abs/2411.00078'><img src='https://img.shields.io/badge/Stage2--Paper-Nat.Comm.Med.-red'></a> 
</p>

### Model Performances 

<p align="center">
  <img src="../assets/performance_rating_results.png" width="800">
</p>

### Data Enrichment for Finetuning 

- We also experimented each annotation enrichment strategy with different dataset scales (25%, 50% ... 100%)

<a name="experiment-table"></a>
<p align="center">
  <img src="../assets/experiment_table.png" width="800">
</p>

### Performance after Finetuning 

- Evaluated on a hold-out test set.

- F1-score across training/annotation strategies

<br>

<p align="center">
  <img src="../assets/results-f1.png" width="800">
</p>

- Full metrics across training/annotation strategies

<p align="center">
  <img src="../assets/f1-recall-prec.png" width="800">
</p>


- Qualitative: Areas of improvement highlighted by rectangles.

<p align="center">
  <img src="../assets/qualitative.png" width="600">
</p>

#### Observation 

- **Baseline performance**, CellViT achieves the highest F1 score of 0.78. Kidney-targeted FMs still required.
- **Fine-tuning with enriched data** improves all three models, with StarDist achieving the highest F1 score of 0.82. 
- **Annotation Enrichment**: Combining <ins>foundation model–generated pseudo-labels</ins> and <ins>a subset of pathologist-corrected hard patches</ins> yields consistent performance gains across all models.


 ### This CellFM-HITL Assessment and Enhancement Framework can be Iterative.

<p align="left">
  <a href='https://arxiv.org/abs/2510.01287'><img src='https://img.shields.io/badge/Stage3--Paper-SPIE-26'></a> 
</p>

- With recent FMs (2025) such as CellViT++[Virchow] and Cellpose-SAM, a portion of the **previously rated “medium” or challenging patches** are now labeled by these newer models (rated as “Good”). 

<br>

<p align="center">
  <img src="../assets/stage3_performance_rating.png" width="500">
</p>

## Implementations and Codes

### 1. Individual Cell FMs Inference and Ratings

  Model | Original Baseline Inference code|
  |:---:|:---:|
  | StarDist (Histo.) | [StarDist Inference](../stage1_paper/stardist-inference-gpu/README.md)|
  | Cellpose  | [Cellpose 2.0 Inference](../stage1_paper/cellpose-inference-gpu/README.md) |
  | CellViT  | [CellViT Inference](../stage1_paper/cellvit-inference-gpu/README.md)|

- We also have the new cell FMs (**Cellpose-SAM, CellViT++ variants released 2024 Aug. - 2025 Aug.**) assessment, in [**stage3_paper folder**](../stage3_paper/).

### 2. Annotate/Curate Data in QuPath 

- Script for converting prediction to geojson (for correction in **QuPath**): [**mask_to_geojson_qupath.py**](../mask_to_geojson_qupath.py).

### 3. Finetuned with Enriched Data 

  Finetuned Models | data processing| Weights from Strategies | Implementations|
  |:---:|:---:|:---:|:---:|
  | StarDist (Histo.) |  RGB | [Easy, Hard, Combined](./model_weights/stardist/)|[stardist_tuned](./stardist_tuned/README.md) |
  |Cellpose Finetuned| DAPI-like | [Easy](./model_weights/cellpose/Easy_100%/) | [cellpose_tuned](./cellpose_tuned/README.md)
  | CellViT   |  RGB |[Combined](https://drive.google.com/file/d/1HUTBoCR5818S7Z7NM_ysxaPn3bSBXXGh/view?usp=drive_link) |[cellvit_tuned](./cellvit_tuned/README.md) |

- Due to storage limits, the **best model weights** are listed above and saved in [model_weights](./model_weights/); all model weights are available on [Google Drive](https://drive.google.com/drive/folders/1ztkcIC63Kjwafq6tHuEnENSdZ8-H3gSz?usp=sharing).

### 4. QuPath-StarDist Models

- StarDist achieves the best performance after fine-tuning on our kidney data. We provide [*"How to installed and use our pretrained models in QuPath"*](../qupath_stardist/README.md) 

- Representative fine-tuned Qupath models in [stardist-qupath](./model_weights/stardist-qupath).

### 5. Weighted Sampling in Training

- **Annotation Types:** We used "easy", "hard"  or a "combined set" of annotations. 

- Combined set is highly imbalanced (more "easy" samples than "hard").

  - We provide dummy hard (`fold_hard`) and easy (`fold_easy`) dataset folders in a [weighted_sampling_examples](weighted_sampling_examples) folder.

  - **Weighted sampling**: The [weighted_sampling.py](./weighted_sampling_examples/weighted_sampling.py) script first concatenates `types.csv` (a list of image path and annotation class-"easy" or "hard") from `fold_easy` and `fold_hard` folders and applies weighted sampling per [Supplementary Information 1](./supp_info.pdf). 

    ```python
      # re-weight each row (sample) after concating types.csv 
      def calculate_class_weights(df, label_column,gamma):
          class_counts = df[label_column].value_counts().to_dict()
          total_samples = len(df)
          class_weights = {cls: total_samples / (gamma * count + (1-gamma)*total_samples) for cls, count in class_counts.items()}
          return class_weights 
      ```
  - The output CSV contains image and label paths for the combined set, ready for constructing training data for combined ("easy" + a small set of "hard") annotation strategy.


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
