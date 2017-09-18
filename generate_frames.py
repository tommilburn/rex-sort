import sys
import os
import glob
import numpy as np
import cv2
from datetime import datetime

print cv2.__version__
startTime = datetime.now()
outcsv = open("frameinfo.csv", "w")

debug = False;

if (len(sys.argv) > 1):
    videoname = sys.argv[1]
else:
    print "requires input video filename as argument"
    sys.exit()

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

print "debug mode? y/n\n"
choice = raw_input().lower()

if(choice in yes):
    debug = True
elif choice in no:
    print "okay, running! starting " + str(datetime.now())
else:
    print "unknown value"
    sys.exit()

print("generate audio? y/n")
choice = raw_input().lower()
if(choice in yes):
    audio = True
    os.system('ffmpeg -i "' + videoname + '" -vn ' + videoname[:-4] + '.wav')
    print("done")
    print "audio filemade in " + str(datetime.now() - startTime)


cap = cv2.VideoCapture(videoname)

frames = {}
frameNumber = 0
lastTime = datetime.now()

#generate png images of the video, embed information about the frame in the png
#also, generate a CSV file that will be useful for working with audio
while(cap.isOpened()):
    if frameNumber % 10000 == 0:
        print str(frameNumber) + " frames analyzed in " + str(datetime.now() - lastTime)
        lastTime = datetime.now()
    ret, frame = cap.read()
    if (type(frame) == type(None)):
        break
    sum = np.sum(frame)
    frameNumber = frameNumber + 1
    s = 'frames/' + str(sum) + ' ' + str(frameNumber) + '.png'
    if not debug:
        cv2.imwrite(s, frame)
    else:
        print(s)
    frames[frameNumber] = sum;

print "frame generation finished in " + str(datetime.now() - lastTime)
lastTime = datetime.now()

framesfolder = './frames/'
counter = 0;
for key, value in sorted(frames.iteritems(), key=lambda (k,v): (v,k)):
    outcsv.write( "%s %s\n" % (key, value))
    oldname = "%s %s.png" % (value, key)
    newname = str(counter).zfill(6) + '.png'
    print framesfolder + oldname + " - > " + framesfolder + newname
    os.rename(framesfolder + oldname, framesfolder + newname)
    counter = counter + 1

print "frame renaming finished in " + str(datetime.now() - lastTime)
lastTime = datetime.now()

cap.release()
cv2.destroyAllWindows()
