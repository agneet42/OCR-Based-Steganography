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

for rows in modified_arr:
	print(rows)

max_one_array = []
for rows in modified_arr:
	max_length = 0
	length = 0
	for val in rows:
		if(val == 0):
			length = 0
		else:
			length = length + 1
			max_length = max(max_length,length)
	max_one_array.append(max_length)

print(max_one_array) # 32-sized vector containing maximum consecutive 1's in a row.