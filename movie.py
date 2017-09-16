import sys
import os
from moviepy.editor import VideoFileClip
import numpy as np
import cv2
from datetime import datetime

print cv2.__version__
print "hello world"
startTime = datetime.now()

rex = VideoFileClip('rex.avi')

final_clip = rex.subclip(1000,1010)
final_clip.write_videofile("rex_test.mp4");
