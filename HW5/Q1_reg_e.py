import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from skimage import data, io, filters
from skimage.feature import match_template
import Q1_reg_c as utils

def replace_occurrances(image,template,indexes,ax):
	width_temp,height_temp,depth=template.shape
	xs,ys,zs=indexes
	
	for i in range(len(xs)):
		pass
		plt.imshow(template,extent=[ys[i], ys[i]+height_temp, xs[i]+width_temp,xs[i]])
		# rect = plt.Rectangle((ys[i],xs[i]), height_temp,width_temp, edgecolor='r',facecolor="None")
		# ax.add_patch(rect)

def run_main():
	the_text= np.asarray(Image.open("Images/Q1/Text.jpg"),dtype=np.float64)/255.0
	c = np.asarray(Image.open("Images/Q1/c.jpg"),dtype=np.float64)/255.0
	k = np.asarray(Image.open("Images/Q1/k.jpg"),dtype=np.float64)/255.0

	ax=plt.subplot(111)
	ax.imshow(the_text)

	# print()

	occ=utils.find_all_occurrances(the_text,c,.876)
	replace_occurrances(the_text,k,occ,ax)
	ax.set_xlim(0, the_text.shape[1])
	ax.set_ylim(the_text.shape[0], 0)
	plt.show()

if __name__ == '__main__':
	run_main()