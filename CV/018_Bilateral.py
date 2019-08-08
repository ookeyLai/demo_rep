# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:15:30 2018

@author: 103009
"""

import numpy as np
import cv2

pic = cv2.imread('data/test.jpg')

dimpixel = 7
color = 100
space = 100
filter = cv2.bilateralFilter(pic,dimpixel,color,space)

cv2.imshow('Filter',filter)
cv2.imshow('Org',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
