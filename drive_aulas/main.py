import cv2 as cv2
import numpy as np

def funcaoMouse(event, x, y, flags, usedata):
    if(event == EVENT_LBUTTONDOWN):
        print("Botão esquerdo clicado - coordenada (" + x + ", " + y + " )")
    else:
        if(event == EVENT_RBUTTONDOWN):
            print("Botão direito clicado - coordenada (" + x + ", " + y + " )")
        else:
            if(event == EVENT_MBUTTONDOWN):
                print("Botão do meio clicado - coordenada (" + x + ", " + y + " )")
            else:
                if(event == EVENT_MOUSEMOVE):
                    print("Movimento do mouse - coordenada (" + x + ", " + y + " )")

img_ir = cv2.imread('open_field.png', 0)

cv2.namedWindow("img", cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('img', funcaoMouse)
cv2.imshow("img", img_ir)

cv2.setMouseCallback("img", funcaoMouse)

