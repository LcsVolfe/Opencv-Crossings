
import cv2
import numpy as np

img_ir = cv2.imread('1.tif', 0)
img_rededge = cv2.imread('2.tif', 0)


cv2.imshow("Imagem", img_ir)
cv2.waitKey(0)
