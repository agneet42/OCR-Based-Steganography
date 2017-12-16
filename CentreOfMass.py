import numpy as numpy
import cv2
from PIL import Image
import os
import skimage
from skimage.feature import daisy
from skimage import data
import matplotlib.pyplot as plt
import csv

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
# for rows in one_a:
#	print(rows)

arr = [one_a,two_a,three_a,four_a]
CM_vector = []
for val in arr:
	Cx = 0
	Cy = 0
	temp_X = 0
	temp_Y = 0
	for row in range(15,-1,-1):
		row_count = 0
		for col in range(0,16):
			if(val[row][col] == 1):
				temp_X = temp_X + row_count # needs division by some factor
			row_count = row_count + 1
	CM_vector.append(temp_X)

	for col in range(0,16):
		col_count = 0
		for row in range(15,-1,-1):
			if(val[row][col] == 1):
				temp_Y = temp_Y + col_count # needs division by some factor
			col_count = col_count + 1
	
	CM_vector.append(temp_Y)

print(CM_vector)