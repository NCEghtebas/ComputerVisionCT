import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from skimage import data, io, filters
from skimage.feature import match_template
import Q1_reg as utils

def run_main():

	t = np.asarray(Image.open("Images/Q1/full_t.jpg"),dtype=np.float64)/255.0
	cap_t = np.asarray(Image.open("Images/Q1/full_cap_t.jpg"),dtype=np.float64)/255.0
	a = np.asarray(Image.open("Images/Q1/full_a.jpg"),dtype=np.float64)/255.0
	cap_a = np.asarray(Image.open("Images/Q1/full_cap_a.jpg"),dtype=np.float64)/255.0
	