# Cellpose Fine-tuning d and Models


## Installation 

1. Create conda env
```bash
conda create -n <env_name> python=3.9
conda activate <env_name> 
```
2. For easier API-based training, we use Cellpose **3.0**, which retains the same model weights as our baseline.
```bash
pip install cellpose==3.0
```
3. Install pytorch and necessary packages 

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu113

pip install matplotlib pillow tqdm pyyaml
```

4. Numpy and Opencv (the following versions should work)
```bash 
pip install numpy==1.23.4 

pip install opencv-python-headless==4.8.1.78 
```

## DAPI-like data prep 

The first band contains the grayscale intensity and the second band is typically unused (set to zeros). This format is compatible with Cellpose 3.0's training and inference APIs.

Update the input_folder and output_folder paths,
```python
if __name__ == "__main__":

    # Paths
    input_folder = '/path/to/rgb/images/folder'             
    output_folder = '/path/to/images_processed/folder'    
    os.makedirs(output_folder, exist_ok=True)
    
    preprocess_image_bands(input_folder, output_folder)

```

then run:
```bash   
python preprocess_image.py
```
Example processed images and their paired labels are provided in [data_dummy](data_dummy). These labels are FM-generated (noted as "easy", or rated as "good" by human).  

```bash
data_dummy
├── train
│   ├── images_processed
│   │   ├── xxx.npy
│   │   └── xxx.npy
|   |   ... 
│   └── labels
│       ├── xxx.npy
│       ├── xxx.npy
|       |...
└── val
    ├── images_processed
    │   └── xxx.npy
    |   ...
    ├── labels
    │   └── xxx.npy
        ... 
```

## Model and Weights 



## Training Instructions 

Our enriched datasets includes "easy" (FMs-generated) annotations, "hard" (pathologist-corrected) annotations, or both. Prepare the training dataset — or your own labeled dataset — in the 2-band ndarray format described in the [DAPI-like data prep section](#dapi-like-data-prep).