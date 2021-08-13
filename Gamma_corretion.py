import os
import numpy as np
import cv2
import tqdm


def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

if __name__ == '__main__':
	input_dir = "/home/datadev/Codes/working_dir/Sasa_sample"
	output_dir = "/home/datadev/Codes/working_dir/improved"
	gama_value = 2.0
	images = [item for item in os.listdir(input_dir)]
	for item in tqdm.tqdm(images):
		img = cv2.imread(os.path.join(input_dir,item))
		# import the necessary packages
		img = adjust_gamma(img, gama_value)
		cv2.imwrite(os.path.join(output_dir,item), img)