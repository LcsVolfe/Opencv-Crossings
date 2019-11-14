import cv2 as cv2
import numpy as np


img = cv2.imread('Quimeras.jpg')
img2 = cv2.imread('Quimeras.jpg')
img3 = cv2.imread('Quimeras.jpg')

def contraste(x):
    global img2, img
    if x>0:
        img2 = cv2.addWeighted

brilho = 100
img2[img2<255-brilho] += brilho
img3[img3<255-brilho] += brilho
img3[img3>255-brilho] = 255
#cv2.imshow('dst',img)
#cv2.imshow('dst2',img2)
#cv2.imshow('dst3',img3)

imgC = cv2.convertScaleAbs(img, alpha=2, beta=50)
cv2.imshow('dst3',imgC)

cv2.waitKey(0)
cv2.destroyAllWindows()