import sys
import os
import glob
import numpy as np
import cv2
from datetime import datetime

print(cv2.__version__)
startTime = datetime.now()


if (len(sys.argv) > 1):
    videoname = sys.argv[1]
else:
    print("requires input video filename as argument")
    sys.exit()

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

debug = False;
print("debug mode? y/n\n")
choice = input().lower()

if(choice in yes):
    debug = True
elif choice in no:
    print("okay, running! starting " + str(datetime.now()))
else:
    print("unknown value")
    sys.exit()

print("generate audio? y/n")
choice = input().lower()
if(choice in yes):
    audio = True
    os.system('ffmpeg -i "' + videoname + '" -vn ' + videoname[:-4] + '.wav')
    print("done")
    print("audio filemade in " + str(datetime.now() - startTime))

cap = cv2.VideoCapture(videoname)

frames = {}
frameNumber = 0
outcsv = open("frameinfo.csv", "w")
lastTime = datetime.now()

#this is the function that actually evaluates and provides a measurement
#based on data about the frame. it's sum right now.
def calculateFrameMetric(frame):
    return np.sum(frame)

#generate png images of the video, embed information about the frame in the png
#also, generate a CSV file that will be useful for working with audio
debugLimit = 0
while(cap.isOpened()):
    if(debug and debugLimit != 0 and frameNumber > debugLimit):
        break
    if frameNumber % 10000 == 0:
        print(str(frameNumber) + " frames analyzed in " + str(datetime.now() - lastTime))
        lastTime = datetime.now()
    ret, frame = cap.read()
    if (type(frame) == type(None)):
        break

    frameMetric = calculateFrameMetric(frame)
    
    frameNumber = frameNumber + 1
    s = 'frames/' + str(frameMetric) + ' ' + str(frameNumber) + '.png'
    if not debug:
        cv2.imwrite(s, frame)
    else:
        print(s)
    frames[frameNumber] = frameMetric;
print("frame generation finished in " + str(datetime.now() - lastTime))
lastTime = datetime.now()

#rename the frames and create the csv file with the frame data
framesfolder = './frames/'
counter = 0;
from collections import OrderedDict
frames = {v: k for k, v in frames.items()}
frames = OrderedDict(sorted(frames.items()))
print(frames)
"""
for key, value in sorted(frames.iteritems(), key=lambda(k,v): (v,k)):
    outcsv.write( "%s %s\n" % (key, value))
    oldname = "%s %s.png" % (value, key)
    newname = str(counter).zfill(6) + '.png'
    print(framesfolder + oldname + " - > " + framesfolder + newname)
    os.rename(framesfolder + oldname, framesfolder + newname)
    counter = counter + 1
print("frame renaming finished in " + str(datetime.now() - lastTime))
lastTime = datetime.now()
"""



#final cleanup
cap.release()
cv2.destroyAllWindows()
