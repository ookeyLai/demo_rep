#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:16:39 2018

@author: ookey
"""

import cv2
import time
import matplotlib.pyplot as plt

def convertToRGB(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

def detect_faces(f_cascade,colored_img,scaleFactor=1.1,minNeighbors=5):
    img_cpoy = colored_img.copy()
    gray = cv2.cvtColor(img_cpoy,cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(gray,scaleFactor=scaleFactor,minNeighbors=minNeighbors)
    for (x,y,w,h) in faces:
        cv2.rectangle(img_cpoy,(x,y),(x+w,y+h),(0,255,0),1)
    return img_cpoy

# main()

haar_face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_alt.xml')
lbp_face_cascade = cv2.CascadeClassifier('data/lbpcascade_frontalface.xml')

test3 = cv2.imread('data/person2_2.jpg')

#faces_detected_img = detect_faces(lbp_face_cascade,test3,1.05,5)
#plt.imshow(convertToRGB(faces_detected_img))

faces_detected_img = detect_faces(haar_face_cascade,test3,1.05,5)
plt.imshow(convertToRGB(faces_detected_img))
    