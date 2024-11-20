# cellpose-inference-gpu
A customized GPU inference code for cell nuclei foundation model - Cellpose
The main script used for performing inference on a directory of PNG files using the Cellpose model: 
```
cellpose_gpu.py
```

## Reference

- Cellpose paper [link](https://www.nature.com/articles/s41592-020-01018-x)
- Cellpose github [link](https://github.com/MouseLand/cellpose)
- This repo is based on the paper: [Assessment of Cell Nuclei AI Foundation Models in Kidney Pathology](https://arxiv.org/abs/2408.06381)


## Requirements

Before running the script, make sure you have the following Python packages installed:
- `numpy`
- `cellpose`
- `PIL` (Pillow)
- `glob`
- `os`
- `tqdm`
- `shutil`
- `random`
- `time`
- `cv2` (OpenCV)
- `pickle`
- `matplotlib`

You can install the required packages using pip:

```bash
pip install numpy cellpose pillow glob2 tqdm opencv-python matplotlib
```

## Usage

### 1. Set Up the Paths

You need to modify the script to set the paths according to your directory structure:

- **`base_image_dir`**: The base directory containing multiple folders of PNG files.
- **`png_subdir_name`**: The specific folder name within the base directory that contains the PNG files you want to process.
- **`output_predictions_dir`**: The directory where the prediction results will be saved.

### 2. Run the Script

To execute the script, run:

```bash
python cellpose_inference.py
```

### 3. Output

The script will save different types of outputs based on the **specified suffix**:

- **Contours Image (`_contours.png`)**: The script overlays contours of detected instances on the original image and saves it as a `.png` file.
- **Binary Mask (`_binary.png`)**: If specified, the script saves a binary mask of the detected instances as a grayscale image.
- **Cell Probability Map (`_cellprob.npy`)**: The script can save the cell nuclei probability map as a `.npy` file.
- **Instance Map (`_contours.npy`)**: The instance segmentation map is saved as a `.npy` file.

### 4. Customizing the Inference Process

You can customize various aspects of the inference process, such as:

- **Model Type**: The model type can be set to `"nuclei"` or any other supported Cellpose model.
- **Channels**: Customize the channels used for inference (e.g., `[0, 0]` for grayscale).
- **Diameter**: Specify the expected diameter of the objects (e.g., 17 pixels for nuclei).
- **Flow Threshold**: Set the flow threshold for mask generation.
- **Minimum Size**: Specify the minimum number of pixels per mask.

### 5. Performance and Runtime

The script outputs the total runtime after processing all images. This can help you estimate the performance for larger datasets.

### 6. Error Handling

If an IO error occurs while processing an image, the script will output an error message indicating the problematic file.

## Example

Here is an example of how the script might be used:

```python
# Base directory containing multiple folders of PNG files
base_image_dir = '/path/to/base/folder'

# Subdirectory within the base directory that contains the PNG files
png_subdir_name  = 'subfolder'

# Output directory for predictions
output_predictions_dir = '/path/to/result'

# Full path to the folder containing the PNG files
png_folder_path = os.path.join(base_image_dir, png_subdir_name)

# Create the output directory if it does not exist
if not os.path.exists(output_predictions_dir):
    os.makedirs(output_predictions_dir)

# Initialize the CellposeProcessor
cp = CellposeProcessor(use_gpu=True, model_type="nuclei")

# Retrieve all PNG files from the specified directory
image_files = glob.glob(os.path.join(png_folder_path, '*.png'))

# Run inference and save the results
cp.inference_instance_loop(image_files=image_files, output_dir=output_predictions_dir, suffix=['_contours.png'])

# Output the total runtime
print(f'run time is {cp.run_time}')
```

This example demonstrates setting up the directories, running the inference, and saving the results.

## License

This script is provided under the MIT License. Please see the LICENSE file for details.
```

You can use this content as your README file to provide clear instructions on how to use the script for performing inference using the Cellpose model.
