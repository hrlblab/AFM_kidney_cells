import numpy as np
from cellpose import models
from PIL import Image
import glob as glob
import os
import cv2

class CellposeProcessor:

    def __init__(self, use_gpu=True, model_type="nuclei"):
        # Initialize the Cellpose model with the specified type and GPU support 
        self.gpu = use_gpu
        self.model = models.Cellpose(model_type=model_type, gpu=use_gpu)

    def model_eval(self, image_array,
                   channels=[0, 0],
                   diameter=None,
                   flow_threshold=0.4,
                   min_size=15,
                   invert=True):

        """
        Perform inference on the provided image array using the Cellpose model.
        
        code reference: cellpose.models.Cellpose.eval() method

        :param  image_array: The image data to be processed 
        :param  channels: 0=grayscale, 1=red, 2=green, 3=blue. (0=None, will set to zero)
        :param  diameter: (30 pixels in the cyto model and 17 pixels in the case of the nuclei model)
        :param  flow_threshold: the maximum allowed error of the flows for each mask. The default is 0.4
        :param  min_size: minimum number of pixels per mask, can turn off with -1 (default 15)
        other params （default）/customized by Cellpose.eval()

        :return:
        Returns
            -------
            masks: list of 2D arrays, or single 3D array (if do_3D=True)
                    labelled image, where 0=no masks; 1,2,...=mask labels

            flows: list of lists 2D arrays, or list of 3D arrays (if do_3D=True)
                flows[k][0] = XY flow in HSV 0-255
                flows[k][1] = XY flows at each pixel
                flows[k][2] = cell probability (if > cellprob_threshold, pixel used for dynamics)
                flows[k][3] = final pixel locations after Euler integration

            styles: list of 1D arrays of length 256, or single 1D array (if do_3D=True)
                style vector summarizing each image, also used to estimate size of objects in image

            diams: list of diameters, or float (if do_3D=True)
        """

        return self.model.eval(image_array, channels=channels, diameter=diameter, flow_threshold=flow_threshold,
                               min_size=min_size, invert=invert)

    def load_image(self, img_path):
        """
        Load an image from the specified path and convert it to an RGB numpy array.

        :param img_path: Path to the image file.
        :return: Numpy array of the RGB image.
        """

        image = np.array(Image.open(img_path).convert('RGB'))
        return image


    def save_plots_grayscale(self, image_array, output_dir):
        """
        :param image_array: 2d image as array
        :param output_dir: complete path for output, e.g., /xxxx_instance.png
        :return: 
        """

        # binary map
        if image_array.ndim == 2:
            binary = np.stack((image_array, image_array, image_array), axis=-1) > 0
            image = Image.fromarray((binary * 255).astype(np.uint8))
            image.save(output_dir)

    def inference_instance_loop(self, image_files, output_dir, binary=False, flow_threshold=0.4, min_size=15):
        """
        Perform inference on a list of PNG images and save results to the specified output directory.
        
        :param image_files: List of file paths to PNG images. Example: ['/directory/to/1.png', '/directory/to/2.png', ... ]
        :param output_dir: Directory where the results will be saved.
        :param binary: Indicating the type of results to save. Can be a semantic (binary=True) or  instance (binary=False) level
        :param  flow_threshold: the maximum allowed error of the flows for each mask. The default is 0.4
        :param  min_size: minimum number of pixels per mask, can turn off with -1 (default 15)


                      
        :return: None
        """
        for image_file in image_files:
            try:
                image = self.load_image(image_file)
                mask, flows, _, _ = self.model_eval(image, channels=[0, 0], diameter=None, flow_threshold=flow_threshold, min_size=min_size,
                                                    invert=True)

                basename = os.path.basename(image_file)

                # save the binary mask as a grayscale image
                if binary:
                    output = os.path.join(output_dir, basename.replace(".png", '_grayscale.png'))
                    self.save_plots_grayscale(mask, output)
                
                # save the instance level output (instance npy mask and contour overlay visual)
                else:
                    unique_labels = np.unique(mask)
                    unique_labels = unique_labels[unique_labels != 0]

                    # get contours of instance predictions
                    for label in unique_labels:
                        binary_mask = np.where(mask == label, 255, 0).astype(np.uint8)
                        contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
                    
                    output = os.path.join(output_dir, basename.replace(".png", '_contours.png'))
                    Image.fromarray(image).save(output)

                    # save instance map as .npy File
                    np.save(output.replace(".png", ".npy"), mask)

            except Exception as e:
                # Handle any IO errors that occur during processing
                print(f'{image_file} has IO error')


if __name__ == "__main__":
    
    # Path/to/image(png)/directory
    image_dir = '/path/to/AFM_kidney_cells/stage1_paper/examples'
    image_files = glob.glob(os.path.join(image_dir, '*.png'))

    # Output directory 
    output_dir = '/path/to/AFM_kidney_cells/stage1_paper/cellpose-inference-gpu/result'
    os.makedirs(output_dir, exist_ok=True)

    # cellpose model init 
    cellpose_model = CellposeProcessor(use_gpu=True, model_type="nuclei")

    # flow_thresh with 0.8 seems to be better for our kidney dataset 
    cellpose_model.inference_instance_loop(image_files=image_files, 
                                            output_dir=output_dir, 
                                            flow_threshold=0.8, 
                                            binary=False)  # binary=True (for semantic seg.)
    


