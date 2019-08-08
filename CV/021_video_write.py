# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:51:02 2018

@author: 103009
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('data/SampleVideo.mp4')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
# fourcc = cv2.VideoWriter_fourcc(*'WMV1')
# fourcc = cv2.VideoWriter_fourcc(*'WMV2')
fourcc = cv2.VideoWriter_fourcc(*'X264') # size smallest

fps = 30
ret,frame = cap.read()
framesize = (frame.shape[1],frame.shape[0])
# framesize = (720,480)

out = cv2.VideoWriter('sample.avi',fourcc,fps,framesize)

while (cap.isOpened()):
    ret, frame = cap.read()
    
    if ret is True:
        frame = cv2.flip(frame,180)
        
        out.write(frame)
        cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
