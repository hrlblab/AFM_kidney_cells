import os
import glob

import numpy as np
from PIL import Image
from csbdeep.utils import normalize
from stardist.models import StarDist2D
import cv2


global BINARY
BINARY = False

class StardistProcessor:
    """
    StardistProcessor is responsible for handling the inference process 
    using a pre-trained StarDist2D model.
    """

    def __init__(self,  model_type="2D_versatile_he", use_gpu=True):
        # Initialize the Stardist2D model with the specified type and GPU support.
        self.gpu = use_gpu
        self.model = StarDist2D.from_pretrained(model_type)

        if self.gpu:
            self.model.config.use_gpu = True


    def model_eval(self, image_array, nms_thresh=None, prob_thresh=None):
        """
        Perform inference on the provided image array using the Stardist model.

        the params are based on Stardist model API,
        Using default values: prob_thresh=0.692478, nms_thresh=0.3
        :param image_array: The image data to be processed.
        :param nms_thresh: Non-Maximum Suppression threshold (optional).
        :param prob_thresh: Probability threshold for object detection (optional).
        :return: Tuple of labels (instance segmentation map) and results
        """

        # normalize channels jointly
        image_array = normalize(image_array, 1, 99.8, axis=(0, 1, 2))

        # model inference
        labels, res = self.model.predict_instances(
            image_array, nms_thresh=nms_thresh, prob_thresh=prob_thresh
        )

        return labels, res

    def load_image(self, img_path):
        """
        Load an image from the specified path and convert it to an RGB numpy array.

        :param img_path: Path to the image file.
        :return: Numpy array of the RGB image.
        """
        image = np.array(Image.open(img_path).convert('RGB'))
        return image


if __name__ == "__main__":

    # Path/to/image(png)/directory
    image_dir = '/path/to/AFM_kidney_cells/stage1_paper/examples'
    image_files = glob.glob(os.path.join(image_dir, '*.png'))

    # Output directory 
    output_dir = '/path/to/AFM_kidney_cells/stage1_paper/stardist-inference-gpu/result'
    os.makedirs(output_dir, exist_ok=True)

    # Initialize the StardistProcessor for model inference
    model = StardistProcessor()

    try:
        for img in image_files:
            # Load the image from file
            image_array = model.load_image(img)


            # Perform model inference to get instance labels and results
            labels, res = model.model_eval(image_array)     # instance map, res

            # Save Binary Mask if BINARY is set to True (default is False)
            if BINARY:
                binary_map = ((labels > 0).astype(np.uint8)) * 255
                output_file = os.path.join(output_dir, os.path.basename(img).replace(".png", "_grayscale.png"))
                if binary_map.ndim != 3:
                    image = Image.fromarray(np.stack((binary_map, binary_map, binary_map), axis=-1))
                    image.save(output_file)

            # Save Instance Mask (Default)
            else:
                unique_labels = np.unique(labels)
                unique_labels = unique_labels[unique_labels != 0]
                for label in unique_labels:
                    binary_mask = np.where(labels == label, 255, 0).astype(np.uint8)
                    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    cv2.drawContours(image_array, contours, -1, (0, 255, 0), 3)
                
                # Save the results: contours visualization (png) and instance labels (npy)
                np.save(os.path.join(output_dir, os.path.basename(img).replace(".png", "_contours.npy")), labels)
                Image.fromarray(image_array).save(os.path.join(output_dir, os.path.basename(img).replace(".png", "_contours.png")))

    except Exception as e:
        print('Error in  ' + img)




