#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:01:18 2018

@author: ookey
"""

import numpy as np
import cv2

# https://github.com/opencv/opencv/tree/master/data/haarcascades
cascade_path = "data/haarcascade_frontalface_default.xml"
# cascade_path = "data/haarcascade_eye.xml"
face_cascade= cv2.CascadeClassifier(cascade_path)

pic = cv2.imread("data/faces.jpg")
scaleFactor = 1.1 # 1.3
minNeighbors = 3 #5

# cv2.imshow("ORG",pic)
# cv2.waitKey(0)

faces = face_cascade.detectMultiScale(pic, scaleFactor, minNeighbors)
print("Member of faces found", (len(faces)))
for (x, y, w, h) in faces:
    cv2.rectangle(pic, (x,y), (x+w, y+h),(255,0,0),2)
        
cv2.imshow("FACES", pic)
cv2.waitKey(0) 
cv2.destroyAllWindows()
