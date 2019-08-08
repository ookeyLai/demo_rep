# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:04:39 2018

@author: 103009
"""

import numpy as np
import cv2

pic = cv2.imread('data/test.jpg')

kernal = 3

# Remove the pixel of noise around the image
median = cv2.medianBlur(pic,kernal)

cv2.imshow('Original',pic)
cv2.imshow('Median',median)

cv2.waitKey(0)
cv2.destroyAllWindows()
