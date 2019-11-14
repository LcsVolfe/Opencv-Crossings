import cv2 as cv
import numpy as np
img = cv.imread('len_top.jpg')
cv.namedWindow('imagem1')
cv.imshow("imagem1", img)
img2 = cv.Canny(img,100,200)
cv.namedWindow('Canny')
cv.imshow("Canny", img2)
cv.waitKey(0)
cv.destroyAllWindows()