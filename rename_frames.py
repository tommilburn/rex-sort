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
