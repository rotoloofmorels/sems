import cv2
import math
import numpy as np
for q in range(0,1) :
    rgb=cv2.imread("rgb"+str(q)+".jpg")#RGB images having blue,green,red band.To be used only in this place
    rgn=cv2.imread("g_r_nir"+str(q)+".jpg")
    rgn1=cv2.imread("g_r_nir"+str(q)+".jpg")
    #cv2.imshow('XXX',rgn)
    hsv=cv2.cvtColor(rgb,cv2.COLOR_BGR2HSV)
    #h,s,v=cv2.split(hsv)
    nir=cv2.imread("nir"+str(q)+".jpg",0)
    #red=cv2.imread("red94.jpg",0)
    vi=cv2.imread("Label_1.png",0)
    conv=cv2.cvtColor(rgb, cv2.COLOR_BGR2YCR_CB)
    y,cr,cb=cv2.split(conv)
    y1=np.asarray(y,np.uint16)
    nir1=np.asarray(nir,np.uint16)
    for i in range(0,360) :
        for j in range(0,480) :
            z=nir1[i][j]
            k=y1[i][j]
            w=(2.7*z+3*k)/5#Dehazing technique of fusing nir and rgb images
            vi[i][j]=w
    f=cv2.merge((vi,cr,cb))
    f1=cv2.cvtColor(f, cv2.COLOR_YCR_CB2BGR)
    f2=cv2.cvtColor(f1, cv2.COLOR_BGR2LAB)
    mask2 = cv2.inRange(f2, (0,-128,-128), (100,128,128))
    ret,mask3=cv2.threshold(nir,30,255,cv2.THRESH_BINARY)
    mask3i=cv2.bitwise_not(mask3)
    mask4=cv2.bitwise_and(mask3i,mask2)
    kernel = np.ones((5,5),np.uint8)
    #o = cv2.morphologyEx(mask4, cv2.MORPH_OPEN, kernel)
    c = cv2.morphologyEx(mask4, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow('A',f1)
    #cv2.imshow('ASD',c)
    #cv2.waitKey(0)
    w=5
    z=vi[0:w,0:w]
    z5=vi[0:10,0:10]
    #print(z.shape)
    for i in range(0,w) :
        for j in range(0,w) :
            z[i][j]=0
    i=0
    j=480
    x1=0.0
    y1=0.0
    z1=0.0
    a1=[]
    a2=[]
    a3=[]
    k=0
    while(i<=360-w) :
        j=480
        while(j>=w) :
            r1=rgn[i:i+w,j-w:j]
            r2=c[i:i+w,j-w:j]
        #print(i,j)
            hist = cv2.calcHist([r2],[0],None,[256],[0,256])
            if(hist[255]==0) :
                j=j-1
                continue
            t1=0.0
            t2=0.0
            t3=0.0
            w1=0.0
            w2=0.0
            w3=0.0
            k=0
            x2,y2,z2=cv2.split(r1)
            for m in range(0,w) :
                for n in range(0,w) :
                    if(r2[m][n]==0) :
                        #print(x2[m][n],y2[m][n],z2[m][n])
                        #x1=x1+x2[m][n]
                        #y1=y1+y2[m][n]
                        #z1=z1+z2[m][n]
                        a1[k]=x2[m][n]
                        a2[k]=y2[m][n]
                        a3[k]=z2[m][n]
                        k=k+1
            #cv2.imshow('PPP',rgn1)
            #cv2.waitKey(0)
            if(k==0):
                cv2.imshow('ASD',r2)
                cv2.waitKey(0)
                continue
            #t1=x1/k
            #t2=y1/k
            #t3=z1/k
            t1=median(a1)
            t2=median(a2)
            t3=median(a3)
            x1=0
            y1=0
            z1=0
        #cv2.waitKey()
            for m in range(0,w) :
                for n in range(0,w) :
                    if(r2[m][n]==0) :
                        w1=w1+(t1-x2[m][n])*(t1-x2[m][n])
                        w2=w2+(t2-y2[m][n])*(t2-y2[m][n])
                        w3=w3+(t3-z2[m][n])*(t3-z2[m][n])
            w1=math.sqrt(w1/k)
            w2=math.sqrt(w2/k)
            w3=math.sqrt(w3/k)
            a=np.uint8()
            b=np.uint8()
            c1=np.uint8()
            #a=int(t1/w1)
            #b=int(t2/w2)
            #c1=int(t3/w3)
            #print(w1,w2,w3)
            for m in range(0,5) :
                for n in range(0,5) :
                    if(r2[m][n]==255) :
                        r1[m][n][0]=int(t1)
                        r1[m][n][1]=int(t2)
                        r1[m][n][2]=int(t3)
        
        #else :
            #cv2.imshow('ASD',r1)
            #cv2.imshow('BBB',r2)
            #cv2.waitKey(0)
            rgn[i:i+w,j-w:j]=r1
            c[i:i+w,j-w:j]=z
            j=j-1
        #print(i,j)
        #cv2.imshow('GHD',ii)
        #cv2.waitKey(0)
        i=i+1
    cv2.imshow('PPP',rgn1)
    cv2.imshow("ASD",rgn)
    #cv2.imshow('WWW',rgn)
    #cv2.waitKey(0)
#Mask is present in c.For regeneration use the images g_r_nir.jpg present in same folder so that regenerated images have same format


#v1=vi
#a=0.0
#b=0.0
#c=0.0 
#i1=np.asarray(nir,np.int16)
#i2=np.asarray(red,np.int16)
#s=np.asarray(s,np.int16)
#v=np.asarray(v,np.int16)
#m=0.0
#n=0.0
#k=0.0
#print(v)
#print()
#print(s)
#print(h)
#for i in range(0,360) :
#    for j in range(0,480) :
#        if(s[i][j]==0 and v[i][j]==0) :
#            v1[i][j]=0
#            continue
#        a=s[i][j]-v[i][j]
#        b=s[i][j]+v[i][j]
#        c=a/b
#        if(c>0.57) :
#            v1[i][j]=255
#        else :
#            v1[i][j]=0
#cv2.imshow('BDB',hsv)
#cv2.imshow('ASD',vi)
#cv2.waitKey(0)
#for i in range(0,360) :
#    for j in range(0,480) :
#        if(i1[i][j]==0 and i2[i][j]==0):
#           vi[i][j]=0
#           continue
#        m=(i1[i][j]-i2[i][j])
#        n=(i1[i][j]+i2[i][j])
#        k=(m/n)
#        if(k>0.5) :
#           vi[i][j]=0
#        else :
#           vi[i][j]=255
#cv2.imshow('BDB',v1)
#cv2.imshow('ASD',vi)
#Ecv2.waitKey(0)
#cv2.imwrite('shadowrecon.jpg',rgn)
k1,k2,k3=cv2.split(rgn)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(k1)
cl2 = clahe.apply(k2)
cl3 = clahe.apply(k3)
img4=cv2.merge((cl1,cl2,cl3))
#cv2.imshow('ASD',rgn)
#cv2.waitKey(0)
