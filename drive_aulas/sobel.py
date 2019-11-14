import cv2, sys
import numpy as np

primeiro=0
segundo=0

def delta(x):
    global img2, img, scale, delta
    primeiro = x    
    img2 = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=5, scale=1, delta=x)    
    cv2.imshow("Sobel", img2)

def scale(x):
    global img2, img, delta, scale
    segundo = x
    img2 = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=5, scale=x, delta=1)    
    cv2.imshow("Sobel", img2)


img = cv2.imread('Quimeras.jpg',0)
cv2.namedWindow('img')
cv2.imshow('img', img)

img2 = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=5, scale=1, delta=1)
cv2.namedWindow('Sobel')

cv2.createTrackbar('Scale','Sobel',0,255, scale)
cv2.createTrackbar('Delta','Sobel',0,255, delta)
cv2.imshow('Sobel', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
