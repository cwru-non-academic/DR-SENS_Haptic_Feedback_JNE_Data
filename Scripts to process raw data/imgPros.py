# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:54:18 2019

@author: Luis
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("S0264.jpg")
imRGB = im.convert('RGB')
image = np.array(imRGB)

i=0;
j=0;

cantFind=0

#pixel cuantities
AllHands = 802927
FrontLeft = 201539
BackLeft = 180962
FrontRight = 201822
BackRight = 207883

#for all color the programs misses around 1.5% of them and does not classify them as anything

color=[]

color1RGB=[150, 50, 250] #purple
color1=[]

color2RGB=[47, 218, 119]#green
color2=[]

color3RGB=[250, 100, 60]#orange
color3=[]

color4RGB=[230, 30, 100]#Fuchsia
color4=[]

color5RGB=[23, 73, 179]#Blue
color5=[]

color6RGB=[19, 102, 45]#dark green not used
color6=[]

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


while i < image.shape[0]:
    while j < image.shape[1]:
        if(compNum(image[i,j,1],image[i,j,0]) and compNum(image[i,j,2],image[i,j,0])):
            Gray = True
            color.append([i,j])
        else:
            # any other color(
            #print(str(image[i,j,0])+","+str(image[i,j,1])+","+str(image[i,j,2]))
            #color.append([i,j])
            if(compNum(image[i,j,0], color1RGB[0]) and compNum(image[i,j,1], color1RGB[1]) and compNum(image[i,j,2], color1RGB[2])):
                color1.append([i,j])
            elif(compNum(image[i,j,0], color2RGB[0]) and compNum(image[i,j,1], color2RGB[1]) and compNum(image[i,j,2], color2RGB[2])):
                color2.append([i,j])
            elif(compNum(image[i,j,0], color3RGB[0]) and compNum(image[i,j,1], color3RGB[1]) and compNum(image[i,j,2], color3RGB[2])):
                color3.append([i,j])
            elif(compNum(image[i,j,0], color4RGB[0]) and compNum(image[i,j,1], color4RGB[1]) and compNum(image[i,j,2], color4RGB[2])):
                color4.append([i,j])
            elif(compNum(image[i,j,0], color5RGB[0]) and compNum(image[i,j,1], color5RGB[1]) and compNum(image[i,j,2], color5RGB[2])):
                color5.append([i,j])
            #elif(compNum(image[i,j,0], color6RGB[0]) and compNum(image[i,j,1], color6RGB[1]) and compNum(image[i,j,2], color6RGB[2])):
                #color6.append([i,j]) dark green not being used
            else:
                #cantfind=True
                #print("color not recognized")     
                #print(image[i,j])
                cantFind = cantFind+1
                
        j=j+1;
    i=i+1;
    j=0;

if((cantFind/len(color))*100 > 2.5):
    print ("High amount of missed pixels. ")
    print (" {0:2.2f} percent of pixels where not categorized. A total of {1:d} pixels where missed.".format(((cantFind/len(color))*100), cantFind ))
    
    
    
c=0
imC = Image.open("empty.jpg")
imCRGB = imC.convert('RGB')
imageC= np.array(imCRGB)
colorArray = np.asarray(color)

while c < colorArray.shape[0]:
    imageC[colorArray[c,0],colorArray[c,1]]= [51, 204, 51]
    c=c+1
 
plt.imshow(imageC)

"""
c=0
imageC= np.array(imCRGB)
colorArray = np.asarray(color1) #replace color one with desired color

while c < colorArray.shape[0]:
    imageC[colorArray[c,0],colorArray[c,1]]= [51, 204, 51]
    c=c+1
 
plt.imshow(imageC)

used this to check fro a specific color by relacing color 1 with what ever color you want to see

"""


