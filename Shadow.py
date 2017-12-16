import numpy as numpy
import cv2
from PIL import Image
import os
import skimage
from skimage.feature import daisy
from skimage import data
import matplotlib.pyplot as plt
import csv


img = cv2.imread('img049-00301.png',0)
res = cv2.resize(img,(32,32))
cv2.imwrite('resized.png',res)
img = skimage.io.imread('resized.png')
modified_arr = []
for rows in img:
	temp_row = []
	for val in rows:
		if(val == 255):
			temp_row.append(0)
		else:
			temp_row.append(1)
	modified_arr.append(temp_row)
	temp_row = []

Matrix = numpy.array(modified_arr)
temp_a, temp_b = numpy.vsplit(Matrix,2)
one_a, two_a = numpy.hsplit(temp_a,2)
three_a, four_a = numpy.hsplit(temp_b,2)

'''from scipy.misc import imshow
imshow(three_a)

for row in three_a:
	print(row)'''

sub_matrices = [one_a,two_a,three_a,four_a]
shadow_vector = []
for val in sub_matrices:
	length_LR = 0
	length_TB = 0
	flag = 0
	for row in range(0,16):
		for col in range(0,16):
			if(val[row][col] == 1 and flag == 0):
				start = row
				flag = 1
				break
			elif(val[row][col] == 1):
				end = row
				break
	length_LR = end - start
	flag = 0
	shadow_vector.append(length_LR)
	for col in range(0,16):
		for row in range(0,16):
			if(val[row][col] == 1 and flag == 0):
				start = col
				flag = 1
				break
			elif(val[row][col] == 1):
				end = col
				break
	length_TB = end - start
	shadow_vector.append(length_TB)

print(shadow_vector)