# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:51:02 2018

@author: 103009
"""

import numpy as np
import cv2
import sys
from pathlib import Path

argc = len(sys.argv)
if argc < 3:
    print("Usage: python %s <input_video_name> <output_video_name> [<output_mode>]" % (sys.argv[0]))
    print("output_mode: XVID | WMV1 | WMV2 | X264(default)")
    sys.exit(0)

inFile = sys.argv[1]
outFile = sys.argv[2]
if argc==4:
    outMode = sys.argv[3]
else:
    outMode = 'X264'

if (not Path(inFile).is_file()):
    print("Error: file %s not exists !!" % (inFile))
    sys.exit(0)

cap = cv2.VideoCapture(inFile)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
# fourcc = cv2.VideoWriter_fourcc(*'WMV1')
# fourcc = cv2.VideoWriter_fourcc(*'WMV2')
# fourcc = cv2.VideoWriter_fourcc(*'X264') # size smallest
fourcc = cv2.VideoWriter_fourcc(*outMode)

fps = 30
ret,frame = cap.read()
framesize = (frame.shape[1],frame.shape[0])
# framesize = (720,480)

out = cv2.VideoWriter(outFile,fourcc,fps,framesize)

i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    
    if ret is True:
        frame = cv2.flip(frame,180)
        
        out.write(frame)
        i += 1
        if i%100 == 1:
            print("Frame:",i//100)
        # cv2.imshow('Frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

out.release()
cap.release()
cv2.destroyAllWindows()
