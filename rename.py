import sys
import operator
import os
import glob
from datetime import datetime

print "hello world"
startTime = datetime.now()
frames = {}
outputfolder = './frames/'
files = glob.glob('./frames/*');
for f in files:
    name = os.path.basename(f)
    s = str.split(name[:-4])
    frames[s[0]] = s[1]

sortedframes = sorted(frames.items(), key=operator.itemgetter(1))

i = 0
for frame in sortedframes:
    oldpath = outputfolder + str(frame[0]) + " " + str(frame[1]) + '.png'
    newpath = outputfolder + str(i) + '.png'
    os.rename(oldpath, newpath)
    i = i + 1
