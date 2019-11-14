import cv2 as cv
import numpy as np
img = cv.imread('len_top.jpg')
cv.namedWindow('imagem')
cv.imshow("imagem", img)
cv.namedWindow('recorte')
cv.namedWindow('resize')
altura, largura = img.shape[0:2]
img2 = img[int(altura*0.15):int(altura*0.85),int(largura*0.15):int(largura*0.85)]
cv.imshow("recorte", img2)
img = cv.resize(img, (0,0), fx=0.75, fy=0.75)
cv.imshow("resize", img)
cv.waitKey(0)
cv.destroyAllWindows()