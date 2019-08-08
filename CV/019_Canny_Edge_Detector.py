# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:24:49 2018

@author: 103009
"""

import numpy as np
import cv2

pic = cv2.imread('data/test.jpg')

threhold_val1 = 100
threhold_val2 = 200

canny = cv2.Canny(pic,threhold_val1,threhold_val2)
# value < threshold_val1 : black
# value > threhold_val2 :white

cv2.imshow('Canny',canny)
cv2.imshow('Org',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
