import cv2 as cv
import imutils

import numpy as np
retangulo = False
x1=0
y1=0
width=0
heigth=0
ini = 0
fim = 0
img = cv.imread('grids_red.png')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# _,img2 = cv.threshold(img,ini,fim,cv.THRESH_BINARY)
# img2 = cv.cvtColor(img2, cv.COLOR_RGB2GRAY)
# ret, img2 = cv.threshold(img2,254,255,cv.THRESH_BINARY)

def nothing(x):
    global img, fim, ini
    fim = x
    img2 = img
    ret, imgnv = cv.threshold(img2,ini,fim,cv.THRESH_BINARY)
    cv.imshow("imagem", imgnv)
def inicio(x):
    global img, fim, ini
    ini = x
    img2 = img
    ret, imgnv = cv.threshold(img2,ini,fim,cv.THRESH_BINARY)
    cv.imshow("imagem", imgnv)


cv.namedWindow('imagem')
# create trackbars for color change
cv.createTrackbar('Fim','imagem',0,255,nothing)
cv.createTrackbar('Inicio','imagem',0,255,inicio)


cv.imshow("imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()
