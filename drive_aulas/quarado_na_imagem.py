import cv2
import numpy as np
from math import sqrt

def desenhaCaixa(img, x, y):
    cv2.rectangle(img, (x+20, y+20), (x-20, y-20), -1)


def funcaoMouse(event, x, y, flags, usedata):
    if(event == cv2.EVENT_LBUTTONDOWN):
        print("Botão esquerdo clicado - coordenada ({0}, {1})". format(x,y) )
        desenhaCaixa(img_ir, x, y )
    elif(event == cv2.EVENT_RBUTTONDOWN):
        print("Botão direito clicado - coordenada ({0}, {1})". format(x,y) )
    elif(event == cv2.EVENT_MBUTTONDOWN):
        print("Botão do meio clicado - coordenada ({0}, {1})". format(x,y) )
    elif(event == cv2.EVENT_MOUSEMOVE):
        print("Movimento do mouse - coordenada ({0}, {1})". format(x,y) )

img_ir = cv2.imread('Quimeras.jpg')

cv2.namedWindow("img")

cv2.setMouseCallback("img", funcaoMouse) 


while True:
    cv2.imshow("img", img_ir)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()