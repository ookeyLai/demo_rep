# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:05:23 2018

@author: 103009
"""

import numpy as np
import cv2

pic = np.zeros((500,500,3),dtype='uint8')

cv2.rectangle(pic,(0,0),(500,150),(123,200,90),3,lineType=0,shift=0)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(pic,'MyText',(100,100),font,3,(255,255,255),3,cv2.LINE_8)
cv2.circle(pic,(250,250),50,(255,0,255))
cv2.line(pic,(133,138),(388,138),(0,0,255))

cv2.imshow('Dark',pic)
cv2.waitKey(0)
cv2.destroyAllWindows()

