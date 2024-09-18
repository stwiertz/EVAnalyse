import cv2 as cv
import numpy as np
from time import time

cap = cv.VideoCapture("./src/Phoenix.mp4")
loop_time = time()
while True:

    ret, frame = cap.read()

    cv.imshow('frame',frame)
    loop_time = time()
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key == ord("p"):
        cv.imwrite('src/recapscreen/positive/{}.jpg'.format(loop_time), frame)
    elif key == ord("n"):
        cv.imwrite('src/recapscreen/negative/{}.jpg'.format(loop_time), frame)