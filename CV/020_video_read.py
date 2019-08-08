# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:33:30 2018

@author: 103009
"""

import numpy as np
import cv2

flag = 0
cap = cv2.VideoCapture('data/SampleVideo.mp4')
while (cap.isOpened()):
    flag = 1
    ret, frame = cap.read()
    if ret is not True:
        break
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        flag = 2
        break
    
cap.release()
print('Flag=',flag)

cv2.destroyAllWindows()

    