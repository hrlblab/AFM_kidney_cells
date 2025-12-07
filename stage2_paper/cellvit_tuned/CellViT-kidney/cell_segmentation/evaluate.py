import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from stardist.matching import matching
from PIL import Image
import glob
import os
import csv
from typing import Set
import argparse

# helper functions
def find_files(directory: str, format: str = '.svs') -> Set[str]:
    """
    Find all folders/subdirectories that contain files with the specified format.
    :param directory: The root directory to search for files.
    :param format: The type of the files to search for (default is '.svs', for the WSI file search).
    :return: A set of directories containing files with the specified format
    """
    svs_directories = set()  # Use a set to store unique parent directories

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(format):
                svs_directories.add(root)  # Use add() to add unique directories

    return svs_directories

class EvaluateParser:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description="Perform CellViT evaluation",
        )


        parser.add_argument(
            "--predictions",
            type = str,
            help="This directory will store predictions (.npy)",
            default = '/home/guoj5/Desktop/200_annotation/temp/cellvit_fold6_latest_723/200_annotation_qa'

        )

        parser.add_argument(
            "--gt",
            type = str,
            help="This directory will store ground-truth",
            default="/home/guoj5/Documents/200_annotation_masks/masks_npy"
        )

        parser.add_argument(
            "--log_csv",
            type = str,
            default=''
        )

        self.parser = parser

    def parse_arguments(self) -> dict:
        opt = self.parser.parse_args()
        return vars(opt)


if __name__ == "__main__":
    config_parser = EvaluateParser()
    config = config_parser.parse_arguments()
    path_to_predictions = config['predictions']
    path_to_groundtruth = config['gt']

    # dataset prediction dir
    data_dirs = list(find_files(path_to_predictions, format='.npy'))
    print(data_dirs)

    # Log csv
    if len(config['log_csv']) > 0:
        file_path = config['log_csv']
        os.makedirs(file_path[0:file_path.find(os.path.basename(file_path))], exist_ok=True)
    else:
        file_path = None

    thresh = 0.5
    for directory in data_dirs:
        print(os.path.basename(directory))
        predictions = glob.glob(os.path.join(directory, '*.npy'))

        Log = []
        for prediction in predictions:
            # /path/to/ground truth
            gt = os.path.join(path_to_groundtruth, prediction.split('/')[-1].replace("_contours.npy", ".npy"))

            # load predictions and ground truth as I1, I2
            I1 = np.load(prediction).astype(np.uint32)
            I2 = np.load(gt)

            # stats object w/t iou=0.5
            stats = matching(y_true=I2, y_pred=I1, thresh=thresh)
            Log.append(
                [directory, prediction.split('/')[-1], stats.f1, stats.precision, stats.recall, stats.panoptic_quality])

    if file_path is not None:
        # Check if the file exists
        if not os.path.exists(file_path):
            # If it doesn't exist, create a new file
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['folder', 'predictions', 'f1', 'precision', 'recall', 'panoptic_quality'])
                for row in Log:
                    writer.writerow(row)

    df = pd.DataFrame(Log, columns=['directory', 'prediction', 'f1', 'precision', 'recall', 'panoptic_quality'])
    print('Mean of each metrics, IoU=0.5')
    print(f'f1: {round(df["f1"].mean(), 4)}')
    print(f'precision: {round(df["precision"].mean(), 4)}')
    print(f'recall: {round(df["recall"].mean(), 4)}')
    print(f'panoptic_quality: {round(df["panoptic_quality"].mean(), 4)}')

    print()
