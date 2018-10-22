import cv2
import numpy as np
img=cv2.imread("Label_3.png")
for i in range(0,360) :
    for j in range(0,480) :
        for k in range(0,3) :
            if(img[i][j][k]==1) :
                img[i][j][k]=0
            else :
                img[i][j][k]=255
cv2.imshow('ASD',img)
cv2.waitKey(0)
