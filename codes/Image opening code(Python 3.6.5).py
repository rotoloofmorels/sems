import numpy as np
import gdal
from gdalconst import *
import cv2
import matplotlib.pyplot as plt
dataset = gdal.Open("to_rvce.tif", GA_ReadOnly )
stats = [dataset.GetRasterBand(i+1).GetStatistics(True, True) for i in range(dataset.RasterCount)]
vmin, vmax, vmean, vstd = zip(*stats)
print(vmax)
#gdal.Translate("output1.tif",dataset,scaleParams=[[65535,0,255,0]])
#data1 = gdal.Open("output1.tif", GA_ReadOnly )
#stats = [data1.GetRasterBand(i+1).GetStatistics(True, True) for i in range(data1.RasterCount)]
#vmin1, vmax1, vmean1, vstd1 = zip(*stats)
#print(vmax1)
data = dataset.ReadAsArray()
d1=data[0]
d2=data[1]
d3=data[2]
d4=data[3]
d5=data[4]
d6=data[5]
d7=data[6]
d8=data[7]
print(data[3][0])
print()
cv2.normalize(d3,d3, alpha=0, beta=65535, norm_type=cv2.NORM_MINMAX)
cv2.normalize(d5,d5,alpha=0,beta=65535,norm_type=cv2.NORM_MINMAX)
cv2.normalize(d7,d7,alpha=0,beta=65535,norm_type=cv2.NORM_MINMAX)
#equ = cv2.equalizeHist(d3)
#img1 = d3.astype(np.uint8)#Issue at this place
img1 = (d3/256).astype('uint8')
img2=(d5/256).astype('uint8')
img3=(d7/256).astype('uint8')
#print(img1[0])
#img2 = d5.astype(np.uint8)#Issue at this place
#img3= d7.astype(np.uint8)#Issue at this place
img=cv2.merge((img1,img2,img3))
#print(img1)
#print(img2)
#print(img3)
#print(img[0])
#cv2.imwrite('asd1.jpg',img1)
#cv2.imwrite('asd2.jpg',img2)
#cv2.imwrite('asd4.jpg',img)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img1)
cl2 = clahe.apply(img2)
cl3 = clahe.apply(img3)
img4=cv2.merge((cl1,cl2,cl3))
cv2.imshow('ASD',img4)
cv2.waitKey(0)
#cv2.imwrite("g.jpg",img4)
#plt.imshow(img)
#plt.show()
#plt.colorbar()
k=0
i=0
j=0
while(i<3600) :
    while(j<5280) :
        i2=img4[i:i+360,j:j+480]
        cv2.imwrite("g_r_nir"+str(k)+".jpg",i2)
        k=k+1
        j=j+480
        print(i,j)
    j=0
    i=i+360
k=0
i=0
j=0
while(i<3600) :
    while(j<5280) :
        i2=cl3[i:i+360,j:j+480]
        #cv2.imwrite("nir"+str(k)+".jpg",i2)
        k=k+1
        j=j+480
        print(i,j)
    j=0
    i=i+360
        


