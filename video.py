import sys


import numpy as np
import cv2
print cv2.__version__

print "hello world"
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    # Display the resulting frame
    cv2.imshow('frame',ret)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
