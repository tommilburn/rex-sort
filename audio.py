import wave
import os
import csv
from datetime import datetime

startTime = datetime.now()


infile = wave.open('rexaudio.wav', 'rb')
outfile = wave.open('rexaudio_out.wav', 'wb')
outfile.setparams(infile.getparams())

with open('frameinfo.csv', 'rb') as csvfile:
    framereader = csv.reader(csvfile, delimiter=' ')
    outfilepointer = 0
    infilepointer = 0
    framesamples = 1.0 / 25.0 * infile.getframerate()
    frameNumber = 0
    lastTime = datetime.now()
    print framesamples
    for row in framereader:
        if frameNumber % 1000 == 0:
            print str(frameNumber) + " frames analyzed in " + str(datetime.now() - lastTime)
            lastTime = datetime.now()

        infilepointer = int(float(row[0]) / 25.0 * infile.getframerate())
        #print infilepointer
        infile.setpos(infilepointer)
        outfile.writeframesraw(infile.readframes(int(framesamples)))
        frameNumber = frameNumber + 1
outfile.close()
infile.close()
print "renaming finished in " + str(datetime.now() - startTime)
