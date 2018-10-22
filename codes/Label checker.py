import cv2
import numpy as np
img=cv2.imread("Label_2.png")
for i in range(0,360) :
    for j in range(0,480) :
        for k in range(0,3) :
            if(img[i][j][k]!=1 and img[i][j][k]!=2) :
                print(img[i][j][k])


