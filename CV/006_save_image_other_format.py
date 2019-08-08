# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:27:28 2018

@author: 103009
"""

import numpy as np
import cv2

img = cv2.imread('data/test.png')
cv2.imshow('Original',img)
img = cv2.imwrite('data/test1.jpg',img)
img1 = cv2.imread('data/test1.jpg')
cv2.imshow('New Image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
