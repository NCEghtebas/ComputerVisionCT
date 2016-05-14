import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from skimage import data, io, filters
from skimage.feature import match_template
import Q1_reg as utils

def run_main():
	c = np.asarray(Image.open("Images/Q1/c.jpg"),dtype=np.float64)/255.0
	k = np.asarray(Image.open("Images/Q1/k.jpg"),dtype=np.float64)/255.0

	ten = np.asarray(Image.open("Images/Q1/Sizes/10.jpg"),dtype=np.float64)/255.0
	twelve = np.asarray(Image.open("Images/Q1/Sizes/12.jpg"),dtype=np.float64)/255.0
	fourteen = np.asarray(Image.open("Images/Q1/Sizes/14.jpg"),dtype=np.float64)/255.0
	sixteen = np.asarray(Image.open("Images/Q1/Sizes/16.jpg"),dtype=np.float64)/255.0
	eleven = np.asarray(Image.open("Images/Q1/Sizes/11.jpg"),dtype=np.float64)/255.0

	pics=[ten,eleven,twelve,fourteen,sixteen]
	labels=["ten","eleven","twelve","fourteen","sixteen"]

	temp_c = utils.c_serif_extract(c)
	temp_k = utils.k_serif_extract(k)

	which,what=utils.choose_from_pics(pics,temp_c)
	utils.show_best_match(pics[which],temp_c)
	print(labels[which],what)

	which,what=utils.choose_from_pics(pics,temp_k)
	utils.show_best_match(pics[which],temp_k)
	print(labels[which],what)

if __name__ == '__main__':
	run_main()