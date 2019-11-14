import cv2, sys
import numpy as np

primeiro=0
segundo=0

def primeiro(x):
    global img2, img, segundo, primeiro
    primeiro = x    
    img2 = cv2.Canny(img, x, segundo )
    cv2.imshow("Canny", img2)

def segundo(x):
    global img2, img, primeiro, segundo
    segundo = x
    img2 = cv2.Canny(img, primeiro, x )
    cv2.imshow("Canny", img2)


img = cv2.imread('open_field.png',0)
cv2.namedWindow('img')
cv2.imshow('img', img)

img2 = cv2.Canny(img, 0, 0)
cv2.namedWindow('Canny')

cv2.createTrackbar('Primeiro','Canny',0,255, primeiro)
cv2.createTrackbar('Segundo','Canny',0,255, segundo)
cv2.imshow('Canny', img2)


cv2.waitKey(0)
cv2.destroyAllWindows()
