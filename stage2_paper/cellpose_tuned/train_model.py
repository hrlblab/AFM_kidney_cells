# import packages 
import os, shutil
import numpy as np
import matplotlib.pyplot as plt
from cellpose import core, utils, io, models, metrics
from cellpose import train
from PIL import Image
import torch
import time 

from glob import glob
from tqdm import tqdm
from pathlib import Path
import datetime

import yaml
import argparse

import warnings
warnings.filterwarnings('ignore')

def load_npy(npy_path):
    out = np.load(npy_path)
    return out


# Initialize the argument parser
parser = argparse.ArgumentParser(description="Segmentation Training Script")

# Add argument for YAML config file
parser.add_argument('--config', type=str, required=True, help="Path to the YAML config file")
args = parser.parse_args()

# Load the YAML file
with open(args.config, 'r') as f:
    config = yaml.safe_load(f)


###  model parameters 
# model name and path
initial_model = 'nuclei' #nuclei
model_name = 'finetuned_model' # model name (saved)

n_epochs = config['n_epochs']
save_every = config['save_every']
batch_size = config['batch_size']
train_dir = config['save_path']     # save path 
os.makedirs(train_dir, exist_ok=True)

# model device 
torch_device = torch.device(config['device'])

Use_Default_Advanced_Parameters = False

lr = config.get('lr', 0.0003)
weight_decay = config.get('wd', 0.0001)
if Use_Default_Advanced_Parameters:
    print('Default advanced parameters enabled')
    lr = 0.1
    weight_decay = 0.0001

# model_path = os.path.join(train_dir, 'cellpose_models/') #change to own save path

# if os.path.exists(os.path.join(model_path, model_name)):
#     print(f'!! WARNING: {model_name} already exists and will be deleted in the following part!')


# data loading 
print('loading training dataset')
image_dir = config['image_dir']
mask_dir = config['mask_dir']

X = sorted(glob(os.path.join(image_dir, '*.npy')))
Y = sorted(glob(os.path.join(mask_dir,'*.npy')))
assert all(Path(x).name.split('.')[0]==Path(y).name.split('.')[0] for x,y in zip(X,Y))

X_new = list(map(load_npy,tqdm(X)))
Y_new = list(map(load_npy,tqdm(Y)))

print('\nloading validation dataset')
val_image_dir = config['val_image_dir']
val_mask_dir = config['val_mask_dir']
X_val= sorted(glob(os.path.join(val_image_dir, '*.npy')))
Y_val = sorted(glob(os.path.join(val_mask_dir,'*.npy')))
assert all(Path(x).name.split('.')[0]==Path(y).name.split('.')[0] for x,y in zip(X_val,Y_val))

X_val_new = list(map(load_npy,tqdm(X_val)))
Y_val_new = list(map(load_npy,tqdm(Y_val)))

train_data, train_labels, test_data, test_labels = X_new, Y_new, X_val_new, Y_val_new
    
# train 
logger = io.logger_setup()
model = models.CellposeModel(gpu=core.use_gpu(), model_type=initial_model, device=torch_device)
channels = [0, 0]

start_time = time.time()
new_model_path = train.train_seg(model.net,
                                 train_data=train_data,
                                 train_labels=train_labels,
                                 test_data=test_data,
                                 test_labels=test_labels,
                                 channels=channels,
                                 save_path=train_dir,
                                 n_epochs=n_epochs,
                                 learning_rate=lr,
                                 weight_decay=weight_decay,
                                 SGD=True,
                                 nimg_per_epoch=None,
                                 model_name=model_name,
                                 save_every=save_every,
                                 batch_size=batch_size)

run_time = datetime.timedelta(seconds=round(time.time() - start_time))
print(f'run time : {run_time}')