import cv2 as cv
import numpy as np
img = cv.imread('len_top.jpg', 0)
cv.namedWindow('imagem1')
cv.imshow("imagem1", img)
cv.namedWindow('imagem')
img = cv.bitwise_not(img)
cv.imshow("imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()