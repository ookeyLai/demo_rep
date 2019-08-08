#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 14:39:29 2018

@author: ookey
"""

import numpy as np
import cv2

template = cv2.imread('data/template.jpg',0)
players = cv2.imread('data/players.jpg',0)

result = cv2.matchTemplate(players, template, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val,max_loc)
cv2.circle(result,max_loc, 15, 255, 2)
cv2.imshow("Matching", result)
cv2.circle(players,max_loc, 15, 255, 2)
cv2.imshow("Players", players)

cv2.waitKey(0)
cv2.destroyAllWindows()
