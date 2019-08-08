# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:59:58 2018

@author: 103009
"""

import numpy as np
import cv2

pic = cv2.imread('data/test.jpg')

matrix = (7,7)
blur = cv2.GaussianBlur(pic,matrix,0)

cv2.imshow('Blur',blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
