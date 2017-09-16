import sys
import os
import glob
import numpy as np
import cv2
from datetime import datetime

print cv2.__version__
print "hello world"
startTime = datetime.now()
outputfolder = './frames'
files = glob.glob('./frames/*')
outcsv = open("out.csv", "w")
for f in files:
    os.remove(f)

cap = cv2.VideoCapture('rex.avi')
frames = {}
frameNumber = 0
while(cap.isOpened()):
    if frameNumber % 1000 == 0:
        print (frameNumber), " frames analyzed"

    ret, frame = cap.read()
    if (type(frame) == type(None)):
        break
#    cv2.imshow('frame',frame)
    sum = np.sum(frame)
#    print frameNumber, sum
    frameNumber = frameNumber + 1
    s = 'frames/' + str(sum) + ' ' + str(frameNumber) + '.png'
#    cv2.imwrite(s, frame)
    frames[frameNumber] = sum;
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        breast = mydict.keys()
for key, value in sorted(frames.iteritems(), key=lambda (k,v): (v,k)):
        outcsv.write( "%s, %s\n" % (key, value))

cap.release()
cv2.destroyAllWindows()
print "analysis finished in " + str(datetime.now() - startTime)

