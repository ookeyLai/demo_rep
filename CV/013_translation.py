# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:15:50 2018

@author: 103009
"""

import numpy as np
import cv2

pic = cv2.imread('data/test.jpg')
cols = pic.shape[1]
rows = pic.shape[0]

# shift right 150 pixs, down 70 pixs
M = np.float32([[1,0,150],[0,1,70]])

shifted = cv2.warpAffine(pic,M,(cols,rows))

cv2.imshow('Shifted',shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()
