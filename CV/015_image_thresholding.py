# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:40:38 2018

@author: 103009
"""

import numpy as np
import cv2

pic = cv2.imread('data/test.jpg',0)
# load pic with 
# 0 => gray scale
# 1 => color

threshold_value = 170
# value < threshold_value = black
# value > threshold_value = white

# (T_value,binary_threshold) = cv2.threshold(pic,threshold_value,255,cv2.THRESH_BINARY)
_,binary_threshold = cv2.threshold(pic,threshold_value,255,cv2.THRESH_BINARY)

cv2.imshow('Binary',binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
