# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:42:15 2018

@author: 103009
"""

import numpy as np
import cv2

pic = np.zeros((500,500,3), dtype='uint8')
color = (255,0,255)

cv2.circle(pic,(250,250),50,color)
cv2.imshow('Dark',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
