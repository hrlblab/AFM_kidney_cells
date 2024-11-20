import os
import random
import shutil
from typing import Set

def copy_random_png_images(source_dir: str, target_dir: str, percentage: int) -> None:

    """
    Randomly copy percentage% png images from source_dir to target_dir
       :param source_dir:
       :param target_dir:
       :param percentage:
       :return:
    """

    for root, dirs, files in os.walk(source_dir):
        for subfolder in dirs:
            source_subfolder = os.path.join(root, subfolder)
            target_subfolder = os.path.join(target_dir, os.path.relpath(source_subfolder, source_dir))
            os.makedirs(target_subfolder, exist_ok=True)

            # List all .png files in the source subfolder
            png_files = [file for file in os.listdir(source_subfolder) if file.lower().endswith(".png")]

            # Calculate the number of .png files to keep
            num_png_files_to_keep = int(len(png_files) * percentage / 100)

            # Randomly select .png files to copy
            png_files_to_copy = random.sample(png_files, num_png_files_to_keep)

            # Copy selected .png files to the target subfolder
            for png_file_to_copy in png_files_to_copy:
                source_png_file = os.path.join(source_subfolder, png_file_to_copy)
                target_png_file = os.path.join(target_subfolder, png_file_to_copy)
                shutil.copy2(source_png_file, target_png_file)


def find_files(directory: str, format: str ='.png') -> Set[str]:
    """

    :param directory:
    :param format:
    :return:
        a Set of strings, which represent the unique sub-folders of files of given format
    """
    png_directories = set()  # Use a set to store unique parent directories

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(format):
                png_directories.add(root)  # Use add() to add unique directories

    return png_directories

