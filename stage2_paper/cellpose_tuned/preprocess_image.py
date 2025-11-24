'''
Preprocess RGB images for Cellpose 3.0 API training and inference.

Specifically, it:
    1. Converts RGB images to grayscale
    2. Normalizes pixel values to [0, 1] range as float32
    3. Creates a two-band array by stacking the grayscale image with a zero-filled band
    4. Saves the result as .npy files with shape (2, height, width)

Input:
    - Folder containing RGB PNG images
    
Output:
    - Folder containing .npy files with shape (2, height, width) as float32 arrays
'''

import os
import numpy as np
from PIL import Image

def preprocess_image_bands(input_folder, output_folder):

    # Iterate through all PNG files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            # Open the image file and convert to grayscale
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path).convert('L')  # Grayscale image
            
            # Convert to numpy array and normalize it to [0, 1] as float32 [normalization] (optional)
            grayscale_array = np.array(img, dtype=np.float32) / 255.0


            # Create a second band filled with zeros of the same shape
            zero_band = np.zeros_like(grayscale_array, dtype=np.float32)

            # Stack the two bands to form a (2, height, width) array
            stacked_array = np.stack([grayscale_array, zero_band], axis=0)

            # Save the array to a .npy file in the output folder with the same filename (but .npy extension)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.npy")
            np.save(output_path, stacked_array)

if __name__ == "__main__":

    # Paths
    input_folder = '/path/to/rgb/images/folder'             #  folder of .png files
    output_folder = '/path/to/images_processed/folder'      #  output folder of .npy files (2, 512, 512) ndarray 

    os.makedirs(output_folder, exist_ok=True)
    preprocess_image_bands(input_folder, output_folder)

    print(f"{input_folder} Conversion to numpy arrays complete!")





