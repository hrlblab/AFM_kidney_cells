# StarDist (Histo.) Fine-tuning and Models

## Requirements

- Python 3.8 and TensorFlow 2.4.4 (the version we use)
- CUDA-compatible GPU (recommended) or CPU
- NVIDIA GPU drivers (for GPU support)

## Installation 

If already created the conda environment and installed packages for stardist inference following the [Step-by-Step Install instructions (option 1)](../../stage1_paper/stardist-inference-gpu/README.md#option-1-step-by-step-install), then only need to install `gputools` for training acceleration.
```bash
pip install gputools==0.2.14
```

## Model Weights and Inference

- Kidney-finetuned StarDist models show improved performance, specially recall and F1 across all three annotation strategies while maintaining high precision. 

- Due to the storage limites, the **best weights** for <ins>each strategy</ins> are provided in [(model_weights/stardist)](../model_weights/stardist/) and available for download on [Google Drive](https://drive.google.com/drive/folders/1ztkcIC63Kjwafq6tHuEnENSdZ8-H3gSz?usp=sharing).

<p align="center">
  <img src="../../assets/stardist_performance.png" width="800">
</p>

## Training Instructions 

### Data and Paths 

Prepare `images` (.png files) and `labels` (.npy files) for both training and validation. Some examples are provided in `data_dummy`.

```bash
train_hard_100
├── images
│   ├── 00295.png
│   ├── ...
├── labels
│   ├── 00295.npy
│   ├── ...

val
├── images
│   ├── xxx.png
│   ├── ...
├── labels
│   ├── xxx.npy
│   ├── ...
```
### Training 

Specifically, assign paths to train, val folders, and output model before running [train_model.ipynb](./train_model.ipynb)

```python
train_image_dir = '/path/to/images' # folder of png files
train_mask_dir = 'path/to/labels'   # folder of npy lables 

val_image_dir = '/path/to/val/images' # folder of png files
val_mask_dir = 'path/to/val/labels'   # folder of npy lables 

model_name = '/path/to/saved/model/folder' # the finetuned model saved here 
```