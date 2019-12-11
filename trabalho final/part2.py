import numpy as np
import cv2

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


img = cv2.imread('img.png')
hsv_frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low_red = np.array([0,120,70])
high_red = np.array([180,255,255])
red_mask = cv2.inRange(hsv_frame, low_red, high_red)
red = cv2.bitwise_and(img, img, mask=red_mask)

height, width, aux = img.shape
x_up, x_down, y_up, y_down = determinarGrids(red_mask,width, height)


cv2.line(img, (x_up[0], 0), (x_down[0], height-1), (255, 100, 0), 3)
cv2.line(img, (x_up[1], 0), (x_down[1], height-1), (255, 100, 0), 3)
cv2.line(img, (0, y_up[0]), (width-1, y_down[0]), (255, 100, 0), 3)
cv2.line(img, (0, y_up[1]), (width-1, y_down[1]), (255, 100, 0), 3)

cv2.imshow('Determinate Grids',img)

cv2.waitKey(0)
cv2.destroyAllWindows()