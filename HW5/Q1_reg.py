import numpy as np
import matplotlib.pyplot as plt 
from PIL import Image
from skimage import data, io, filters
from skimage.feature import match_template

def c_serif_extract(image):
	'''Takes an np image array'''
	x,y, z = image.shape
	template = image[int(.35*x):int(.65*x), int(.6*y):y]
	return template

def k_serif_extract(image):
	x,y, z = image.shape
	template = image[int(.8*x):int(1*x), int(0*y):int(.6*y)]
	return template

#compares template to image and gives measure of how close they are
def apply_template(image,template):
	result = match_template(image, template)
	ij = np.unravel_index(np.argmax(result), result.shape)
	return result[ij]

def show_best_match(image,template):
	result = match_template(image, template)
	ij = np.unravel_index(np.argmax(result), result.shape)
	z, y,x = ij[::-1]
	width_temp,height_temp,depth=template.shape
	# print(x,y,z)
	ax = plt.subplot(111)
	ax.imshow(image)
	# print(x,y)
	# print(width_temp,height_temp,depth)
	rect = plt.Rectangle((y,x), height_temp,width_temp, edgecolor='r',facecolor="None")
	ax.add_patch(rect)
	plt.show()

def choose_from_pics(images,template):
	results=map(lambda img:apply_template(img,template),images)
	which=np.argmax(results)
	what=results[which]
	return (which, what)

def run_main():
	c = np.asarray(Image.open("Images/Q1/c.jpg"),dtype=np.float64)/255.0
	k = np.asarray(Image.open("Images/Q1/k.jpg"),dtype=np.float64)/255.0

	ariel = np.asarray(Image.open("Images/Q1/Fonts/Ariel.jpg"),dtype=np.float64)/255.0
	calibari = np.asarray(Image.open("Images/Q1/Fonts/Calibari.jpg"),dtype=np.float64)/255.0
	plantinoLino = np.asarray(Image.open("Images/Q1/Fonts/PlatinoLinotype.jpg"),dtype=np.float64)/255.0
	timesNewRoman = np.asarray(Image.open("Images/Q1/Fonts/TimesNewRoman.jpg"),dtype=np.float64)/255.0
	verdana = np.asarray(Image.open("Images/Q1/Fonts/Verdana.jpg"),dtype=np.float64)/255.0

	pics=[ariel,calibari,plantinoLino,timesNewRoman,verdana]
	labels=["ariel","calibari","plantinoLino","timesNewRoman","verdana"]

	temp_c = c_serif_extract(c)
	temp_k = k_serif_extract(k)

	which,what=choose_from_pics(pics,temp_c)
	show_best_match(pics[which],temp_c)
	print(labels[which],what)

	which,what=choose_from_pics(pics,temp_k)
	show_best_match(pics[which],temp_k)
	print(labels[which],what)

if __name__ == '__main__':
	run_main()


# plt.imshow(temp_k)
# plt.imshow(temp_c)
# plt.show()