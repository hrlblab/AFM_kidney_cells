import numpy as np
from cellpose import models
from PIL import Image
import glob as glob
import os
from tqdm import tqdm
import cv2
import torch
from pathlib import Path


data_dir = '/path/to/images_processed'  # path to processed images (dapi-like)
rgb_dir = '/path/to/png/folder'         # path to rgb image files directory 
output_dir = '/path/to/output'          # inference output directory 
model_path = '/path/to/weight/folder/finetuned_model'   # path to the finetuned model 
# example: model_path = '/path/to/stage2_paper/model_weights/cellpose/Easy_100%/finetuned_model'

os.makedirs(output_dir, exist_ok=True)

X = sorted(glob.glob(os.path.join(data_dir, '*.npy')))
Y = sorted(glob.glob(os.path.join(rgb_dir,'*.png')))
assert all(Path(x).name.split('.')[0]==Path(y).name.split('.')[0] for x,y in zip(X,Y))

# eval parameters 
channels = [0, 0]
use_GPU=True
diameter = 17   # default diam_mean for 'nuclei' model 
flow_threshold = 0.4 # default is 0.4  
invert=False # default 
min_size = 15
device = torch.device("cuda:0") #default 0

for i in tqdm(range(len(X))):
    image_file = X[i]
    rgb_file = Y[i]
    assert Path(image_file).name.split('.')[0]==Path(rgb_file).name.split('.')[0]

    image_array = np.load(image_file) # processed 2-bands image 
    image = np.array(Image.open(rgb_file).convert('RGB')) # rgb image 

    model = models.CellposeModel(gpu=use_GPU, pretrained_model=model_path, device=device) 
    mask, flows, styles = model.eval(image_array, channels=channels, diameter=diameter, flow_threshold=flow_threshold,
                            min_size=min_size, invert=invert)

    # prediction masks post-processing 
    unique_labels = np.unique(mask)
    unique_labels = unique_labels[unique_labels != 0]

    # get contours of instance predictions
    for label in unique_labels:
        binary_mask = np.where(mask == label, 255, 0).astype(np.uint8)
        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

    Image.fromarray(image).save(os.path.join(output_dir, Path(X[i]).name.split('.')[0] + '_contours.png'))
    
    # save instance map as .npy File
    np.save(os.path.join(output_dir, Path(X[i]).name.split('.')[0] + '_contours.npy'), mask)
