#!/usr/bin/env python
""" Get the input dir and copy all files inside into output_dir and in different subfolders
    based on number of files you give as input
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

def get_file_name(file_list):
    for item in file_list:
        try:
            yield item
        except StopIteration:
            break


if __name__ == '__main__':

    input_dir = "/media/vahid/Elements/Data/berlin/bundles000004" # path to the folder including the files needed to
    output_dir = "/media/vahid/Elements/Data/berlin/rty" # Path to output dir
    max_file_number = 20 # maximum number of files to be copied into

    available_files = [item for item in os.listdir(input_dir)]
    print(f"Total available_files : {len(available_files)}")

    output_folders_num = int(len(available_files)/max_file_number) if len(available_files)%max_file_number == 0 \
        else int(len(available_files)/max_file_number)+1
    print(f"Total output folders {output_folders_num} with {max_file_number} files in each")

    file_name_generator = get_file_name(available_files)# Create generator

    for i in range(output_folders_num):
        print(f"Copy {max_file_number} files into folder {i}")
        # Create the folder inside out_dir
        output_path = os.path.join(output_dir, str(i))
        os.mkdir(output_path)
        j=0
        for file_name in file_name_generator:
            if j == max_file_number:
                break
            else:
                j += 1
                shutil.copyfile(os.path.join(input_dir,file_name),os.path.join(output_path,file_name))

