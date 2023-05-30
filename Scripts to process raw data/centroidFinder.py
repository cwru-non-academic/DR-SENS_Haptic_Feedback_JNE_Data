# -*- coding: utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("empty.jpg")
imRGB = im.convert('RGB')
image = np.array(imRGB)

sub = ["01","02","03","04","05","06","08","09","10","11","12"]
locationList = ["1", "4", "7"]
strenghtList = ["1", "2"]
CordY= 630
totalpixels=0
valMetric =0



def compNum(new, original):
    if(new>100):
        upper = original*1.3
        lower = original*0.7
    else:
        upper = original+40
        lower = original-40
    if new >= lower:
        if new <= upper:
            return True
    return False

def procImage(img, colorImg):
    im = Image.open(img+".jpg")
    imRGB = im.convert('RGB')
    image = np.array(imRGB)
    i=0;
    j=0;
    while i < image.shape[0]:
        while j < image.shape[1]:
            if(compNum(image[i,j,1],image[i,j,0]) and compNum(image[i,j,2],image[i,j,0])):
                Gray = True
            else:
                # any other color
                colorImg[i][j]=(colorImg[i][j])+1
            j=j+1;
        i=i+1;
        j=0;
    return colorImg;
        
def centroid(selected, i):
    distance= CordY-i
    metric =distance*selected
    global valMetric
    valMetric=valMetric+metric
    
        
def batch(location, strenght):
    totalImages=0
    im = Image.open("empty.jpg")
    imRGB = im.convert('RGB')
    image = np.array(imRGB)
    colorIM = [0] * image.shape[0]
    for i in range(image.shape[0]):
        colorIM[i] = [0] * image.shape[1]
    for trial in range(len(sub)):
        name="S"+sub[trial]+location+strenght
        colorIM = procImage(name, colorIM)
        totalImages=totalImages+1
        #print(str(totalImages)+" images processed")
    
    print("processing output")
    #shows results 
    imC = Image.open("empty.jpg")
    imCRGB = imC.convert('RGB')
    imageC= np.array(imCRGB)
    colorArray = np.asarray(colorIM)
    
    i=0
    j=0
    while i < colorArray.shape[0]:
        while j < colorArray.shape[1]:
            if colorArray[i,j] > 0:
                #print("color")
                if 500 < i <1000:
                    global totalpixels
                    totalpixels=totalpixels+1
                    centroid(colorArray[i][j], i)
            j=j+1
        i=i+1
        j=0
 
    
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["2", "3","5", "6","8", "9"]
CordY= 630
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
    
        
sub = ["01", "02","03","04","10","11","12"]
locationList = ["1", "2","3","4","5","6","7","8","9"]
strenghtList = ["1", "2","3"]

