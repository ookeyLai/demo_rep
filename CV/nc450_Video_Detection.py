#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:37:13 2018

@author: ookey
"""

import numpy as np
import cv2
import sys

dev = 0
#dev = 'rtsp://ikare99:ikare8899@[10.100.0.90]:554/h264_hd.sdp'
#dev = 'http://icam.ikare99.25u.com/zm/cgi-bin/nph-zms?scale=50&amp;width=1280px&amp;height=720px&amp;mode=jpeg&amp;maxfps=30&amp;monitor=5&amp;auth=b2a5de09c7f313843c42e4f64e8e4906&amp;connkey=963674&amp;rand=1527051806'
#dev = 'rtsp://ikare99:ikare8899@[10.100.0.90]:554/h264_vga.sdp'
#dev = 'http://ikare99:ikare8899@10.100.0.90:8080/stream/video/h264?resolution=HD'
#dev = 'http://ikare99:ikare8899@10.100.0.90:8080/stream/video/mjpeg?resolution=HD'
argc = len(sys.argv)
if argc > 1:
    if sys.argv[1] == '1':
        dev = 1

cap = cv2.VideoCapture(dev)

while 1:
    ret, pic = cap.read()
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    
    out = pic
    #out = gray
    
    out = (255 - out)
    cv2.imshow("NC450", out)
    
    if (cv2.waitKey(10)&0xFF == ord('q')):
        break
    
cap.release()
cv2.destroyAllWindows()
