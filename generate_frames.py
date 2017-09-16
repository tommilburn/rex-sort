import sys
import os
import glob
import numpy as np
import cv2
from datetime import datetime

print cv2.__version__
print "hello world"
startTime = datetime.now()
outcsv = open("out.csv", "w")

cap = cv2.VideoCapture('rex.avi')
#cv2.imshow(cap)
frames = {}
frameNumber = 0
while(cap.isOpened()):
    if frameNumber % 1000 == 0:
        print (frameNumber), " frames analyzed"

    ret, frame = cap.read()
    if (type(frame) == type(None)):
        break
    sum = np.sum(frame)
#    print frameNumber, sum
    frameNumber = frameNumber + 1
    s = 'frames/' + str(sum) + ' ' + str(frameNumber) + '.png'
    cv2.imwrite(s, frame)
    frames[frameNumber] = sum;

for key, value in sorted(frames.iteritems(), key=lambda (k,v): (v,k)):
        outcsv.write( "%s, %s\n" % (key, value))

cap.release()
cv2.destroyAllWindows()
print "analysis finished in " + str(datetime.now() - startTime)

