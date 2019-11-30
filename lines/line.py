import cv2 
import numpy as np 

img = cv2.imread('grids_red.png') 
GRID_SIZE = 500
print(type(img))
height, width, channels = img.shape

cv2.line(img, (300, 0), (300, height), (255, 0, 0), 11)



cv2.imshow('Hehe', img)
key = cv2.waitKey(0)


