import numpy as np
import cv2
import imutils


img = cv2.imread('img.png')

#  APLICA TRATAMENTO PARA BINARIZAR IMAGEM
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(blurred, 30, 255, cv2.THRESH_BINARY_INV)[1]

# ENCONTRA CONTORNOS NA IMAGEM
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# LOOP NO CONTORNO PARA ENCONTRAR O CENTER_ID
for c in cnts:
    # ENCONTRA O CENTRO DA IMAGEM
    M = cv2.moments(c)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        cX, cY = 0, 0    
    
    # DESENHA ENCIMA DO CENTER_ID
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.circle(thresh, (cX, cY), 7, (255, 255, 255), -1)
    cv2.putText(img, "center", (cX - 20, cY - 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
cv2.imshow('Object Position',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
