import cv2 as cv
import numpy as np
img = cv.imread('len_top.png')
cv.namedWindow('imagem')
cv.namedWindow('imagem2')
cv.namedWindow('imagem3')
img2 = cv.imread('len_top.png')
img3 = cv.imread('len_top.png')
brilho = 100
img2[img2<255-brilho]+=brilho
img3[img3<255-brilho]+=brilho
img3[img3>255-brilho]=255
cv.imshow("imagem", img)
cv.imshow("imagem2", img2)
cv.imshow("imagem3", img3)
cv.waitKey(0)
cv.destroyAllWindows()