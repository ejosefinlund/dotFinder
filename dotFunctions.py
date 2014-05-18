# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 18:20:38 2014

@author: josefin
"""
import numpy as np
from sets import Set



    
foundDotPixels = Set([])
nbrOfBlobs = 0

#converts an rgb or black and white image to a black and white image.jjj
def rgbToBW(rgbIm, height, width) :
    #print rgbIm
    bwPic = np.zeros((height,width))
    for n in range (0,height):
        for i in range (0,width):
            bwPic[n,i] = np.max(rgbIm[n,i])
 
    return bwPic
        
#def firstDotPixel(bwIm, height, width):
#    for n in range (0, width):
#        for i in range (0, height):
#            if ((bwIm[n,i] > 10) and ((n,i) in foundDotPixels) == False):
#                investigateDot(n,i)
#    return -1
#    
        
#search through image after pixels in the color of the cells.
#check if they already belong to foundCellPixels
#if not: send to investigator method.
def investigateDot(n,i):
    foundDotPixels.add((n,i))
    return -1