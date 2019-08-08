# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:46:54 2018

@author: 103009
"""

import numpy as np
import cv2

pic = np.zeros((500,500,3),dtype='uint8')

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic,'My Text',(110,110),font,3,(155,155,155),4,cv2.LINE_4)
cv2.putText(pic,'My Text',(100,100),font,3,(255,255,255),4,cv2.LINE_4)

cv2.imshow('Dark',pic)

cv2.waitKey(0)
cv2.destroyAllWindows()
