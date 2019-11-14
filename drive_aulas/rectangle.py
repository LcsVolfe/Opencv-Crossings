import cv2 as cv
import numpy as np
retangulo = False
x1=0
y1=0
width=0
heigth=0
ini = fim = 0
img = cv.imread('basketball.jpeg')
def nothing(x):
    global img, fim, ini
    fim = x
    img2 = img
    ret, imgnv = cv.threshold(img2,ini,fim,cv.THRESH_BINARY)
    cv.imshow("imagem", imgnv)
def inicio(x):
    global img, fim, ini
    ini = x
    img2 = img
    ret, imgnv = cv.threshold(img2,ini,fim,cv.THRESH_BINARY)
    cv.imshow("imagem", imgnv)
def desenhaCaixa():
    global img, x1, y1, width, heigth
    cv.rectangle(img, (x1, y1), (x1+width, y1+heigth), (255,0,0))
    cv.imshow("imagem", img)
def funcaoMouse(event, x, y, flags, userdata):
    global retangulo, x1, y1, width, heigth, img
    if event == cv.EVENT_LBUTTONDOWN:
        retangulo = True
        x1 = x
        y1 = y
        width =0
        heigth =0
        print("Botao esquerdo clicado - coordenada ({0}, {1})".format(x, y))
    elif event == cv.EVENT_LBUTTONUP:
        retangulo = False
        if width < 0:
            x1 = x1 + width
            width = width * -1
        if heigth < 0:
            y1 = y1 + heigth
            heigth = heigth * -1
        desenhaCaixa()
        print("Botao direito clicado - coordenada ({0}, {1})".format(x, y))
    elif event == cv.EVENT_MBUTTONDOWN:
        print("Botao do meio clicado - coordenada ({0}, {1})".format(x, y))
    elif event == cv.EVENT_MOUSEMOVE:
        if retangulo:
            width = x - x1
            heigth = y - y1
        print("Movimento do mouse - coordenada ({0}, {1})".format(x, y))


cv.namedWindow('imagem')
cv.setMouseCallback('imagem', funcaoMouse, img)
# create trackbars for color change
cv.createTrackbar('Fim','imagem',0,255,nothing)
cv.createTrackbar('Inicio','imagem',0,255,inicio)
img2 = img
cv.imshow("imagem", img2)
cv.waitKey(0)
cv.destroyAllWindows()