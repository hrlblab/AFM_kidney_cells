import os
import cv2
import glob
import json 

import numpy as np
from PIL import Image
from csbdeep.utils import normalize
from stardist.models import StarDist2D
import argparse
from tqdm import tqdm 


global BINARY
BINARY = False


class StardistProcessor:

    def __init__(self,  model_type="2D_versatile_he", use_gpu=True):
        self.gpu = use_gpu
        self.model = StarDist2D.from_pretrained(model_type)

        if self.gpu:
            self.model.config.use_gpu = True


    def model_eval(self, image_array, nms_thresh=None, prob_thresh=None):
        """
        Evaluate/Inference the stardist model on image_array.

        the params are based on Stardist model API,
        Using default values: prob_thresh=0.692478, nms_thresh=0.3
        :param image_array:
        :param nms_thresh:
        :param prob_thresh:
        :return:
        """

        # normalize channels jointly
        image_array = normalize(image_array, 1, 99.8, axis=(0, 1, 2))

        # model inference
        labels, res = self.model.predict_instances(
            image_array, nms_thresh=nms_thresh, prob_thresh=prob_thresh
        )

        return labels, res

    def load_image(self, img_path):
        image = np.array(Image.open(img_path).convert('RGB'))
        return image


if __name__ == "__main__":

    # Parse command line arguments
    parser = argparse.ArgumentParser(description='StarDist inference with custom model')
    parser.add_argument('--model_dir', type=str, required=True,
                        help='Path to the model directory containing thresholds.json')
    parser.add_argument('--image_dir', type=str, default='/path/to/images/folder',
                        help='Path to input images directory')
    parser.add_argument('--output_dir', type=str, default='/path/to/output/folder',
                        help='Path to output directory')
    args = parser.parse_args()

    # Path/to/image(png)/directory
    image_dir = args.image_dir
    image_files = glob.glob(os.path.join(image_dir, '*.png'))

    # Output directory
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    # Read thresholds from thresholds.json in model_dir
    model_dir = args.model_dir
    thresholds_path = os.path.join(model_dir, 'thresholds.json')
    
    if not os.path.exists(thresholds_path):
        raise FileNotFoundError(f"thresholds.json not found in {model_dir}")
    
    with open(thresholds_path, 'r') as f:
        thresholds = json.load(f)

    # load model parameters (nms and prob)
    nms_thresh = thresholds['nms']
    prob_thresh = thresholds['prob']

    # initialize model 
    model = StardistProcessor()
    model.model = StarDist2D(config=None, name=model_dir)
 

    # inference 
    try:
        for i in tqdm(range(len(image_files))):
            
            img = image_files[i]
            image_array = model.load_image(img)

            # Image error
            if np.mean(image_array) < 20:
                print(f"Image error, intensity is too low, check {img}\n")
                continue

            labels, res = model.model_eval(image_array, nms_thresh=nms_thresh, prob_thresh=prob_thresh)     # instance map, res


            # Save Binary mask (default: False)
            if BINARY:
                binary_map = ((labels > 0).astype(np.uint8)) * 255
                output_file = os.path.join(output_dir, os.path.basename(img).replace(".png", "_grayscale.png"))
                if binary_map.ndim != 3:
                    image = Image.fromarray(np.stack((binary_map, binary_map, binary_map), axis=-1))
                    image.save(output_file)

            # Save Instance mask (default: True)
            else:
                unique_labels = np.unique(labels)
                unique_labels = unique_labels[unique_labels != 0]
                for label in unique_labels:
                    binary_mask = np.where(labels == label, 255, 0).astype(np.uint8)
                    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                    cv2.drawContours(image_array, contours, -1, (0, 255, 0), 3)

                # Save the results - both numpy (instance map) and png (contours overlay visualization)
                np.save(os.path.join(output_dir, os.path.basename(img).replace(".png", "_contours.npy")), labels)
                Image.fromarray(image_array).save(os.path.join(output_dir, os.path.basename(img).replace(".png", "_contours.png")))

    except Exception as e:
        print('Error in  ' + img)

    print("Inference Finished")



