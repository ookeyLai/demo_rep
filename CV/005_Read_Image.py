# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:21:56 2018

@author: 103009
"""

import numpy as np
import cv2

img = cv2.imread('data\\test.jpg')
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

