import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from skimage import data, io, filters
from skimage.feature import match_template

def find_all_occurrances(image,template,threshold,):
	result = match_template(image, template)
	indexes=np.where(result > threshold)
	return indexes

def plot_occurrances(image,template,indexes,ax):
	width_temp,height_temp,depth=template.shape
	xs,ys,zs=indexes
	
	for i in range(len(xs)):
		rect = plt.Rectangle((ys[i],xs[i]), height_temp,width_temp, edgecolor='r',facecolor="None")
		ax.add_patch(rect)


def run_main():

	the_text= np.asarray(Image.open("Images/Q1/Text.jpg"),dtype=np.float64)/255.0

	t_tail=np.asarray(Image.open("Images/Q1/t_tail.jpg"),dtype=np.float64)/255.0

	t = np.asarray(Image.open("Images/Q1/full_t.jpg"),dtype=np.float64)/255.0
	cap_t = np.asarray(Image.open("Images/Q1/full_cap_t.jpg"),dtype=np.float64)/255.0
	a = np.asarray(Image.open("Images/Q1/full_a.jpg"),dtype=np.float64)/255.0
	cap_a = np.asarray(Image.open("Images/Q1/full_cap_a.jpg"),dtype=np.float64)/255.0
	
	ax=plt.subplot(111)
	ax.imshow(the_text)

	occ=find_all_occurrances(the_text,cap_t,.9)
	plot_occurrances(the_text,cap_t,occ,ax)
	print("T:"+str(len(occ[0])))

	occ=find_all_occurrances(the_text,t,.89)
	plot_occurrances(the_text,t,occ,ax)
	print("t:"+str(len(occ[0])))

	occ=find_all_occurrances(the_text,cap_a,.9)
	plot_occurrances(the_text,cap_a,occ,ax)
	print("A:"+str(len(occ[0])))

	occ=find_all_occurrances(the_text,a,.84)
	plot_occurrances(the_text,a,occ,ax)
	print("a:"+str(len(occ[0])))

	plt.show()
	# utils.show_best_match(the_text,cap_t)

if __name__ == '__main__':
	run_main()