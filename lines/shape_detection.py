import numpy as np
import cv2
import imutils
import time

cap = cv2.VideoCapture('v.mp4')



contador = 0
ultimoGridVisitado = 0


def conferirIndicesArray(arr, novoValor):    
    if (arr[-1]+100) < novoValor:
        return True
        # print (valor, novoValor, '\n' )


def determinarGrids(frame, width, height):
    grids_x_up = []
    grids_x_down = []
    grids_y_up = []
    grids_y_down = []
    for x in range(width):
        if x+15 < width:
            if frame[0, x] == 0:
                if frame[0, x+1] == 255 and frame[0, x+10] == 255:
                    if len(grids_x_up) == 0:
                        grids_x_up.append(x)
                    elif conferirIndicesArray(grids_x_up, x):
                        grids_x_up.append(x)
                
                if frame[height-1, x+1] == 255 and frame[height-1, x+8] == 255:
                    if len(grids_x_down) == 0:
                        grids_x_down.append(x)
                    elif conferirIndicesArray(grids_x_down, x):
                        grids_x_down.append(x)
                    
                  
    for y in range(height):
        if y+15 < height:
            if frame[0, y] == 0:
                if frame[y+1, 0] == 255 and frame[y+5, 0] == 255:
                    if len(grids_y_up) == 0:
                        grids_y_up.append(y)
                    elif conferirIndicesArray(grids_y_up, y):
                        grids_y_up.append(y)
                    
                if frame[y+1,width-1] == 255:
                    if len(grids_y_down) == 0:
                        grids_y_down.append(y)
                    elif conferirIndicesArray(grids_y_down, y):
                        grids_y_down.append(y)
                                            
                   
    return grids_x_up, grids_x_down, grids_y_up, grids_y_down
    

while(cap.isOpened()):
    ret, frame = cap.read()
    height, width, aux = frame.shape
    frame_drawable = frame    
    
    # THRESHOULD PARA DETERMINAR GRIDS 
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_red = np.array([0,120,70])
    high_red = np.array([180,255,255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    gray = cv2.cvtColor(red, cv2.COLOR_RGB2GRAY)
    gray_thresh = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)[1]

    # cv2.imshow("Image", gray_thresh)
    
    x_up, x_down, y_up, y_down = determinarGrids(gray_thresh,width, height)
    
    # print('x_up',x_up, '----')
    # print('x_down',x_down, '----')
    # print('x_up',y_up, '---')
    # print('x_down',y_down, '\n')
    
    if len(x_up) > 1 and len(x_down) > 1 and len(y_up) > 1 and len(y_down) > 1:    
        cv2.line(frame_drawable, (x_up[0], 0), (x_down[0], height-1), (255, 100, 0), 3)
        cv2.line(frame_drawable, (x_up[1], 0), (x_down[1], height-1), (255, 100, 0), 3)
        cv2.line(frame_drawable, (0, y_up[0]), (width-1, y_down[0]), (255, 100, 0), 3)
        cv2.line(frame_drawable, (0, y_up[1]), (width-1, y_down[1]), (255, 100, 0), 3)
    
        # APLICA TRATAMENTO PARA BINARIZAR IMAGEM
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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
            cv2.drawContours(frame_drawable, [c], -1, (0, 255, 0), 2)
            cv2.circle(thresh, (cX, cY), 7, (255, 255, 255), -1)
            cv2.putText(frame_drawable, "center", (cX - 20, cY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
            
            if gray_thresh[cY, cX] == 0:
                
                print(ultimoGridVisitado, ' ultimoGridVisitado ')
                print(cY > y_up[1], cY , y_up[1], ' cY > y_up[1] 3')
                print(cY > y_up[0], cY , y_up[0], ' cY > y_up[0] 2')
                print(cY < y_up[0], cY , y_up[0], ' cY < y_up[0] 1')
                
                # 3 linha
                if cY > y_up[1] and ultimoGridVisitado != 3:
                    # print(' 3 linha \n')
                    ultimoGridVisitado=3
                    contador = contador+1
                
                # 2 linha
                elif cY > y_up[0] and cY > y_up[1] and ultimoGridVisitado != 2:
                    ultimoGridVisitado=2
                    # print(' 2 linha \n')
                    contador = contador+1
                    
                # 1 linha
                elif cY < y_up[0] and ultimoGridVisitado != 1:
                    # print('1 linha \n')        
                    ultimoGridVisitado=1
                    contador = contador+1
                else:
                    print('else')
                print(contador, 'count \n')
                
                time.sleep(1)
            
            cv2.putText(frame_drawable, ("Contador: " + str(contador)), (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)   
            
            cv2.imshow("Image", frame_drawable)
        
        
        # cv2.imshow('frame',thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # print(contador)
 
cap.release()
cv2.destroyAllWindows()