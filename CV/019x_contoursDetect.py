#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:01:56 2018

@author: ookey
"""

import numpy as np
import cv2

img = cv2.imread("data/detect_blob.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Thresh img", thresh)

_, contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 255, 0)
cnt = 0

objects = np.zeros([img.shape[0],img.shape[1],3], "uint8")
for c in contours:
    cv2.drawContours(objects, [c], -1, color, -1)
    
    area = cv2.contourArea(c)
    if area > 1.0:
        perimeter = cv2.arcLength(c, True)
        cnt += 1
        M = cv2.moments(c)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00']) 
        cv2.circle(objects, (cx, cy), 4, (0,0,255), -1)
    
        print("{}. Area: {}, perimter: {}".format(cnt, area, perimeter))

cv2.imshow("Contours img",objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
