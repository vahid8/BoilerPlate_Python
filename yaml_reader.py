#////////////////////////////// Python -> yaml_reader.py
import yaml
# //////////////////////////  Read the yaml file and load the inputs config /////////////////////////////
with open(r'config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

source_img_folder = config["images_folders"]



#//////////////////yaml file -> config.yaml
# Input Directories
image_path: "/media/vahid/Elements/Data/sample_images/trimble_pano"
detection_path: "/media/vahid/Elements/Data/sample_images/trimble_pano_detection"
output_image_path: "/media/vahid/Elements/Data/sample_images/ready/images"
output_detection_path: "/media/vahid/Elements/Data/sample_images/ready/texts"
cores: 1
# Output Directories to save the images
DIR_OUT: "/media/vahid/Elements/Hamburg_dataset/Folder2/debug/splited5"
