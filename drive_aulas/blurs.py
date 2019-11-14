import cv2 as cv
import numpy as np
img = cv.imread('open_field.png')
cv.namedWindow('imagem1')
cv.imshow("imagem1", img)
img2 = cv.GaussianBlur(img,(7,7),0)
cv.namedWindow('GaussianBlur')
cv.imshow("GaussianBlur", img2)
img2 = cv.medianBlur(img, 5)
cv.imshow("medianBlur", img2)
cv.waitKey(0)
cv.destroyAllWindows()