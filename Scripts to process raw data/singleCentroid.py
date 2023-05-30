# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv

im = Image.open("empty.jpg")
imRGB = im.convert('RGB')
image = np.array(imRGB)

sub = ["01","02","03","04","05","06","08","09","10","11","12"]
locationList = ["1","4","7"]
strenghtList = ["1", "2"]
CordY= 685
totalpixels=0
valMetric =0
minPx=0
maxPx=0
outputFileName = 'centroid_data.csv'

color1RGB=[150, 50, 250] #purple1
color2RGB=[130, 90, 119]#purple2

with open(outputFileName, mode='w',  newline='') as centroid_file:
    centroid_writer = csv.writer(centroid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    centroid_writer.writerow(['subject', 'location', 'strenght', 'centroid', 'min', 'max'])


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

def procImage(img, colorM):
    im = Image.open("empty.jpg")
    imRGB = im.convert('RGB')
    image = np.array(imRGB)
    #make sure to start with empty image to not carry information from previous trial comment if you want to carry and uncomment bellow
    #colorMat = colorImg
    colorMat = np.array([0]*(image.shape[1]*image.shape[0])).reshape(image.shape[0],image.shape[1])
    im = Image.open(img+".jpg")
    imRGB = im.convert('RGB')
    image = np.array(imRGB)
    i=0;
    j=0;
    while i < image.shape[0]:
        while j < image.shape[1]:
            if(compNum(image[i,j,1],image[i,j,0]) and compNum(image[i,j,2],image[i,j,0])):
                Gray = True #shades of white black and gray so do not count up
            else:
                if outputFileName == 'centroid_data.csv' or outputFileName == 'centroid_dataRefElectrode.csv':
                    # any other color
                    colorMat[i][j]=(colorMat[i][j])+1 #all colors 
                else :
                    # if you want a specific color in this case two shades of purple
                    if(compNum(image[i,j,0], color1RGB[0]) and compNum(image[i,j,1], color1RGB[1]) and compNum(image[i,j,2], color1RGB[2])):
                        colorMat[i][j]=(colorMat[i][j])+1
                    elif(compNum(image[i,j,0], color2RGB[0]) and compNum(image[i,j,1], color2RGB[1]) and compNum(image[i,j,2], color2RGB[2])):
                        colorMat[i][j]=(colorMat[i][j])+1
            j=j+1;
        i=i+1;
        j=0;
    return colorMat
        
def centroid(selected, i):
    distance= CordY-i
    metric =distance*selected
    global valMetric, totalpixels, minPx, maxPx 
    valMetric=valMetric+metric
    if minPx == 0:
        minPx = distance
    if maxPx == 0:
        maxPx == distance
    if distance < minPx:
        minPx = distance
    elif distance > maxPx:
        maxPx = distance
        
def batch(location, strenght):
    global valMetric, totalpixels, minPx, maxPx
    totalImages=0
    im = Image.open("empty.jpg")
    imRGB = im.convert('RGB')
    image = np.array(imRGB)
    colorM = np.array([0]*(image.shape[1]*image.shape[0])).reshape(image.shape[0],image.shape[1])
    for trial in range(len(sub)):
        name="S"+sub[trial]+location+strenght
        colorM = procImage(name, colorM)
        totalImages=totalImages+1
        #print(str(totalImages)+" images processed")
    
        print("processing output")
        #shows results 
        imC = Image.open("empty.jpg")
        imCRGB = imC.convert('RGB')
        imageC= np.array(imCRGB)
        #colorArray = np.asarray(colorM)
        colorArray = colorM
    
        i=0
        j=0
        while i < colorArray.shape[0]:
            while j < colorArray.shape[1]:
                if colorArray[i,j] > 0:
                    #print("color")
                    if 500 < i <1000:
                        if 250 < j < 1000:
                            totalpixels=totalpixels+1
                            centroid(colorArray[i][j], i)
                j=j+1
            i=i+1
            j=0
        with open(outputFileName, mode='a',  newline='') as centroid_file:
            centroid_writer = csv.writer(centroid_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            centroid_writer.writerow([sub[trial], location, strenght, valMetric/totalpixels, minPx, maxPx])
        print("centroid for strenght " + str(strenght)+", location "+ str(location)+" and subject :"+ str(sub[trial]) + "= "+str(valMetric/totalpixels))
        valMetric =0
        totalpixels = 0
        minPx = 0
        maxPx = 0
            
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["2", "3","5", "6","8", "9"]
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["1","4","7"]
outputFileName = 'centroid_dataMaxSensation.csv'
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["2", "3","5", "6","8", "9"]
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["1","4","7"]
CordY= 685
outputFileName = 'centroid_dataRefElectrode.csv'
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["2", "3","5", "6","8", "9"]
CordY= 630
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["1","4","7"]
CordY= 685
outputFileName = 'centroid_dataRefElectrodeMaxSens.csv'
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["2", "3","5", "6","8", "9"]
CordY= 630
        
for loc in range(len(locationList)):
    for stren in range(len(strenghtList)):
        batch(locationList[loc], strenghtList[stren])
        #print("centroid for strenght " + str(strenghtList[stren])+" and location "+ str(locationList[loc])+" = "+str(valMetric/totalpixels))
        totalpixels=0
        valMetric = 0
        
locationList = ["1","2","3","4","5","6","7","8","9"]