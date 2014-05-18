# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 18:00:38 2014

@author: josefin
"""
from PIL import Image as im
import numpy as np
import dotFunctions as df
limit = 30 #Pixles with values under 30 will be considered part of dot

try:
    pic = im.open("sampleDot.jpg")
except:
    print "Unable to load image"
    
height = pic.size[0]
width = pic.size[1]
picarray = np.asarray(pic)

bwPicArray = df.rgbToBW(picarray, height,width) #Make image black-white 
pic = im.fromarray(bwPicArray)

#iniate cell count on bwPicArray