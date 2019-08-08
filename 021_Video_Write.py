import numpy as np
import cv2
cap = cv2.VideoCapture('SampleVideo.mp4')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc = cv2.VideoWriter_fourcc(*'WMV1')
#fourcc = cv2.VideoWriter_fourcc(*'WMV2')
fourcc = cv2.VideoWriter_fourcc(*'X264')
fps = 30
#
ret, frame = cap.read()
# height , width , layers =  frame.shape
framesize = (frame.shape[1], frame.shape[0])
# framesize = (720, 480)
#

out = cv2.VideoWriter('Sample5.avi', fourcc, fps, framesize)

i=0
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret is True:
        frame = cv2.flip(frame, 180)

        # write the flipped frame
        out.write(frame)
        i += 1
        print("frames:",i)

        # cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
