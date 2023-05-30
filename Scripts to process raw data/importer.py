# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:59:39 2022

@author: lemfn
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

im = Image.open("S0581.jpg")
imRGB = im.convert('RGB')
image = np.array(imRGB)