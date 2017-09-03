import sys
import numpy as np
import cv2
print cv2.__version__
print "hello world"

cap = cv2.VideoCapture('rex.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    print np.sum(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
