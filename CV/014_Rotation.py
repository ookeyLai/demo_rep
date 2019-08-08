# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:32:44 2018

@author: 103009
"""

import numpy as np
import cv2

pic = cv2.imread('data/test.jpg')
rows = pic.shape[1]
cols = pic.shape[0]

center = (cols/2,rows/2)
angle = 90

M = cv2.getRotationMatrix2D(center,angle,0.5)
# angle,2 to double size of origin, or 0.5 for half size

rotate = cv2.warpAffine(pic,M,(cols,rows))

cv2.imshow('Rotate',rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()
