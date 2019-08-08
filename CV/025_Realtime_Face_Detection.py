#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:37:13 2018

@author: ookey
"""

import numpy as np
import cv2

haar_cascade_path = "data/haarcascade_frontalface_default.xml"
lbp_cascade_path = "data/lbpcascade_frontalface.xml"
# cascade_path = "data/haarcascade_eye.xml"
haar_face_cascade= cv2.CascadeClassifier(haar_cascade_path)
lbp_face_cascade= cv2.CascadeClassifier(lbp_cascade_path)

cap = cv2.VideoCapture(0)

scale_factor = 1.2
minNeighbors = 5
lscale_factor = 1.1
lminNeighbors = 3

while 1:
    ret, pic = cap.read()
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    haar_faces = haar_face_cascade.detectMultiScale(gray, scale_factor,minNeighbors)
    lbp_faces = lbp_face_cascade.detectMultiScale(gray, lscale_factor,lminNeighbors)
    
    for (x,y,w,h) in haar_faces:
        # cv2.rectangle(pic, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.circle(pic,(x+w//2,y+h//2),(w+h)//3,(0,0,255),2)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(pic,"Me",(x+w//4,y),font,2,(255,255,255),2,cv2.LINE_AA)     
    
    for (x,y,w,h) in lbp_faces:
        # cv2.rectangle(pic, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.circle(pic,(x+w//2,y+h//2),(w+h)//3,(0,255,0),2)
        # font = cv2.FONT_HERSHEY_COMPLEX
        # cv2.putText(pic,"Me",(x+w//4,y),font,2,(255,255,255),2,cv2.LINE_AA)
        
    print("Member of faces fount {},{} ".format(len(haar_faces),len(lbp_faces)))
    cv2.imshow("Face", pic)
    
    if (cv2.waitKey(10)&0xFF == ord('q')):
        break
    
cap.release()
cv2.destroyAllWindows()
