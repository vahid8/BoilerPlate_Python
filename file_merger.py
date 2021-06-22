#!/usr/bin/env python
""" Get the input dir and copy all images inside it and all subfolders into one
    output folder without any subfolder
"""

import os
import yaml
import tqdm
import shutil

__author__ = "vahid jani"
__copyright__ = "Copyright 2021, The Blurring Project"
__credits__ = ["Vahid jani"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Vahid jani"
__email__ = "aghajanivahid1@gmail.com"
__status__ = "Development"

if __name__ == '__main__':
    # //////////////////////////  Read the yaml file and load the inputs config /////////////////////////////
    with open(r'subfolders_merger_config.yaml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    input_path = config["input_path"]
    output_path = config["output_path"]

    # Get all files
    folders = [item[0] for item in os.walk(input_path)]

    # iterate over folders including root
    images_paths = []
    for num, folder in enumerate(folders):
        list_of_images = [os.path.join(folder, item) for item in os.listdir(folder) if item.endswith(".jpg")]
        print("{}. Number of images in folder [{}] : {}".format(num+1, folder, len(list_of_images)))
        images_paths.extend(list_of_images)

    print("Total images : {}".format(len(list_of_images)))
    for item in tqdm.tqdm(list_of_images):
        dst = os.path.join(output_path,os.path.basename(item))
        shutil.copyfile(item, dst)

    all_images = [item for item in os.listdir(output_path) if item.endswith(".jpg")]
    print("Total available images after coping into one folder are :{}".format(len(all_images)))