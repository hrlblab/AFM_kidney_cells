# Read Me
A customized GPU inference pipeline for cell nuclei foundation model - StarDist (H&E)

The main script is `stardist_gpu.py`. The detailed description of how to use this GPU-based StarDist codebase is provided below.

## Reference:
- The StarDist paper: [StarDist Paper](https://arxiv.org/abs/2203.02284)
- The StarDist GitHub codebase: [StarDist GitHub](https://github.com/stardist/stardist)
- This repo is based on the paper: [Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology](https://arxiv.org/abs/2408.06381)

## Requirements
Before running the script, ensure you have the following Python packages installed:
- `numpy`
- `PIL` (Pillow)
- `csbdeep` (follow this [link](https://github.com/CSBDeep/CSBDeep/tree/main/extras#conda-environment) for installation, I used the tensorflow 2.4 version)
- `stardist`
- `tqdm`
- `cv2` (OpenCV)
- `matplotlib`
  
The requirements.txt (or environment.yml) is the exported environment file for my conda environment setup

## Usage

### 1. Configure Input and Output Paths
Modify the script to set your paths:
- **`base_image_dir`**: The base directory containing multiple folders of PNG files.
- **`png_subdir_name`**: The specific folder name within the base directory that contains the PNG files you want to process.
- **`output_predictions_dir`**: The directory where the prediction results will be saved.

### 2. Run the Script

Execute the script by running:

```bash
python stardist_inference.py
```

### 3. Output

For each image in the input folder:
- **Contours Image**: A `.png` file with the original image overlaid with contours of detected instances.
- **Instance Mask**: A `.npy` file containing the instance segmentation map.
- **Binary Mask** (optional): If `BINARY` is set to `True`, a binary mask is also saved as a `.png` file.

### 4. Customizing Inference Parameters

You can customize the inference by modifying the following parameters in the script:
- **`model_type`**: The type of StarDist2D model to use (default is `"2D_versatile_he"`).
- **`use_gpu`**: Set to `True` to enable GPU usage if available.
- **`nms_thresh`**: Non-Maximum Suppression threshold (optional).
- **`prob_thresh`**: Probability threshold for object detection (optional).

### 5. Error Handling

If an image is found to be corrupted or unreadable (e.g., very low average pixel value), the script will skip that image and continue processing the remaining images.

### 6. Performance
The total processing time will be printed to the console after the script has finished running.

## Example

Here is an example of how the script might be used:

```python
# Base directory containing multiple folders of PNG files
base_image_dir = '/path/to/base/'

# Subdirectory within the base directory that contains the PNG files
png_subdir_name = 'folder1'

# Output directory for predictions
output_predictions_dir = '/path/to/result'

# Full path to the folder containing the PNG files
png_folder_path = os.path.join(base_image_dir, png_subdir_name)

# Initialize the StardistProcessor for model inference
model = StardistProcessor()

# Create the output directory if it does not exist
if not os.path.exists(output_predictions_dir):
    os.makedirs(output_predictions_dir)

# Retrieve all PNG files from the specified directory
image_files = glob.glob(os.path.join(png_folder_path, '*.png'))

# Run the inference and save the results
for img in image_files:
    image_array = model.load_image(img)
    labels, res = model.model_eval(image_array)
    np.save(os.path.join(output_predictions_dir, os.path.basename(img).replace(".png", "_contours.npy")), labels)
    Image.fromarray(image_array).save(os.path.join(output_predictions_dir, os.path.basename(img).replace(".png", "_contours.png")))

# Output the total processing time
print(time.time() - start_time)
```

