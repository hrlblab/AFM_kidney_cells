# Run Cellpose-SAM for nuclei segmentation

- Run Cellpose-SAM for nuclei segmentation on a folder of images

- This script is adapted from the official Cellpose-SAM Colab notebook by Marius Pachitariu, Michael Rariden, and Carsen Stringer.
It supports batch processing of .png or .tif images using GPU acceleration.

## Setup 
```
pip install git+https://github.com/mouseland/cellpose.git
pip install matplotlib tqdm numpy
```
## Usage:
    python run_cellpose_sam.py --input_dir /path/to/images --output_dir /path/to/output --ext .png

### Alternative: run_Cellpose_SAM.ipynb
