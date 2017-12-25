from PIL import Image
import cv2
import numpy as numpy
import skimage
from skimage import data
import matplotlib.pyplot as plt
import csv

img = cv2.imread('modified.png',0)
res = cv2.resize(img,(800,800))
cv2.imwrite('resized.png',res)
im = skimage.io.imread('resized.png')
for j in range(0,800):
	for i in range(0,800):
		im[i][j] = 255 - im[i][j]
skimage.io.imsave('resized.png',im)
im = cv2.imread('resized.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
count = 1
for val in contours:
	x,y,w,h = cv2.boundingRect(val)
	img = cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
	roi = im[y:y+h, x:x+w]
	cv2.imwrite("%s.png"%(count),roi)
	count = count + 1
