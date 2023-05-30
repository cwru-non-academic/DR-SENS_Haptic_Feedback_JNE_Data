# -*- coding: utf-8 -*-

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("empty.jpg")
imRGB = im.convert('RGB')
image = np.array(imRGB)
colorIM = [0] * image.shape[0]

im = Image.open("empty.jpg")
imRGB = im.convert('RGB')
image = np.array(imRGB)
colorIM = [0] * image.shape[0]
for i in range(image.shape[0]):
   colorIM[i] = [0] * image.shape[1]
    
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
       if i%685 == 0:
           #print("color")
           imageC[i][j] = [0,255,0]
       if i%630 == 0:
           #print("color")
           imageC[i][j] = [0,255,0]    
       j=j+1
   i=i+1
   j=0
 
plt.imshow(imageC)
plt.savefig("resultssqures.png", dpi = 2000)
