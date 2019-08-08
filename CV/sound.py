#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 13:58:31 2018

@author: ookey
"""

frequence = 1000 # hertz
duration = 2000 # millisecond

# Windows
"""
import winsound
winsound.Beep(frequence, duration)
"""

# SoX must be installed: sudo apt-get install sox
# Linux
import os
os.system('play -n synth %s sin %s' % (duration/1000, frequence) )
os.system('spd-say "Your program has finished"')
