import csv
import os
from datetime import datetime

startTime = datetime.now()
frames = {}
framesfolder = './frames/'
counter = 0;
with open('frameinfo.csv', 'rb') as csvfile:
    framereader = csv.reader(csvfile, delimiter=' ')
    for row in framereader:
        oldname = row[1] + ' ' + row[0] + '.png'
        newname = str(counter).zfill(6) + '.png'
        print oldname + " -> " + newname
        counter = counter + 1
        os.rename(framesfolder + oldname, framesfolder + newname)

'''
for frame in sortedframes:
    oldpath = outputfolder + str(frame[0]) + " " + str(frame[1]) + '.png'
    newpath = outputfolder + str(i) + '.png'
    os.rename(oldpath, newpath)
    i = i + 1
'''
print "renaming finished in " + str(datetime.now() - startTime)
