import sys
import os
import glob
import numpy as np
import cv2
from datetime import datetime

print(cv2.__version__)
start_time = datetime.now()


if (len(sys.argv) > 1):
    video_name = sys.argv[1]
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
    os.system('ffmpeg -i "' + video_name + '" -vn ' + video_name[:-4] + '.wav')
    print("done")
    print("audio filemade in " + str(datetime.now() - start_time))

cap = cv2.VideoCapture(video_name)

frames = {}
frame_number = 0
lastTime = datetime.now()

#this is the function that actually evaluates and provides a measurement
#based on data about the frame. it's sum right now.
def calculateFrameMetric(frame):
    return np.sum(frame)

#generate png images of the video, embed information about the frame in the png
debugLimit = 100
while(cap.isOpened()):
    if(debugLimit != 0 and frame_number > debugLimit):
        break
    if frame_number % 10000 == 0:
        print(str(frame_number) + " frames analyzed in " + str(datetime.now() - lastTime))
        lastTime = datetime.now()
    ret, frame = cap.read()
    if (type(frame) == type(None)):
        break

    frameMetric = calculateFrameMetric(frame)
    
    frame_number = frame_number + 1
    s = 'frames/' + str(frameMetric) + ' ' + str(frame_number) + '.png'
    if not debug:
        cv2.imwrite(s, frame)
    else:
        print(s)
    frames[frame_number] = frameMetric;
print("frame generation finished in " + str(datetime.now() - lastTime))
lastTime = datetime.now()

#rename the frames and create the dict with the frame data
framesfolder = './frames/'
counter = 0;
from collections import OrderedDict
frames = {v: k for k, v in frames.items()}
sorted_frames = OrderedDict(sorted(frames.items()))
pad_length = len(str(len(sorted_frames)))
print(pad_length)
for frame_info, frame_number in sorted_frames.items():
    print(frame_info, frame_number)
    oldname = "%s %s.png" % (frame_info, frame_number)
    newname = str(counter).zfill(pad_length) + '.png'
    print(framesfolder + oldname + " - > " + framesfolder + newname)
    os.rename(framesfolder + oldname, framesfolder + newname)
    counter = counter + 1

print("frame renaming finished in " + str(datetime.now() - lastTime))
lastTime = datetime.now()

#final cleanup
cap.release()
cv2.destroyAllWindows()
