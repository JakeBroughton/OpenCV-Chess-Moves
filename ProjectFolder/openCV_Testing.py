# Ideas
# Detect chess moves through camera

import numpy as np
import cv2

filename = "testimage.png"
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)  # img, blockSize, ksize, k

dst = cv2.dilate(dst, None)

img[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

"""
img = np.zeros((512,512,3), np.uint8)

img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

cv2.imshow("frame", img)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()


img = cv2.imread('testimage.png', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27: # Escape key
    cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)

while True:
    # Capture frames
    ret, frame = cap.read()

    # Operations on the frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the result
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""