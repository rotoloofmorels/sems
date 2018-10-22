import cv2
import numpy as np
img=cv2.imread("Label_1.png")
z=np.zeros((360,480),np.uint8)
for i in range(0,360) :
    for j in range(0,480) :
        if(img[i][j][0]==2) :
            z[i][j]=0
        else :
            z[i][j]=255
kernel = np.ones((5,5),np.uint8)
o = cv2.morphologyEx(z, cv2.MORPH_OPEN, kernel)
c = cv2.morphologyEx(o, cv2.MORPH_CLOSE, kernel)
hist = cv2.calcHist([c],[0],None,[256],[0,256])
print("Ideal")
print("Lakes Area :")
print(hist[255]/(36*48))
print("Non lakes Area :")
print(hist[0]/(36*48))
img1=cv2.imread("seg1.jpeg",0)
ret,bg=cv2.threshold(img1,130,255,cv2.THRESH_BINARY)
cv2.imshow('ASD',bg)
cv2.imwrite('seg123.jpg',bg)
#gray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
t=0
p=0
i=0
o = cv2.morphologyEx(bg, cv2.MORPH_OPEN, kernel)
c = cv2.morphologyEx(o, cv2.MORPH_CLOSE, kernel)
hist = cv2.calcHist([bg],[0],None,[256],[0,256])
print()
print("Predicted")
print("Lakes Area :")
print(hist[255]/(36*48))
print("Non lakes Area :")
print(hist[0]/(36*48))
