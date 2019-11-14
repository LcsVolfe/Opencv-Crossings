import cv2 as cv
import numpy as np
def funcaoMouse(event, x, y, flags, userdata):
    if event == cv.EVENT_LBUTTONDOWN:
        print("Botao esquerdo clicado - coordenada ({0}, {1})".format(x, y))
    elif event == cv.EVENT_RBUTTONDOWN:
        print("Botao direito clicado - coordenada ({0}, {1})".format(x, y))
    elif event == cv.EVENT_MBUTTONDOWN:
        print("Botao do meio clicado - coordenada ({0}, {1})".format(x, y))
    elif event == cv.EVENT_MOUSEMOVE:
        print("Movimento do mouse - coordenada ({0}, {1})".format(x, y))
img = cv.imread('basketball.jpeg')
cv.namedWindow('imagem')
cv.setMouseCallback('imagem', funcaoMouse)
cv.imshow("imagem", img)
cv.waitKey(0)
cv.destroyAllWindows()