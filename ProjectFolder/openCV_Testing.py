import numpy as np
import cv2

# # filename = "test_images/blank_board.jpg"
# filename = 'test_images/real_board.jpg'
#
# # Base image
# imgBase = cv2.imread(filename)
#
# cv2.imshow("Base Image", imgBase)
#
# # Edge detection
# img = cv2.imread(filename)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Make grayscale
#
# gray = np.float32(gray)  # Corner harris method needs float32 format
#
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)  # img, blockSize, ksize, k
#
# dst = cv2.dilate(dst, None)
#
# img[dst > 0.01*dst.max()] = [0, 0, 255]
#
# cv2.imshow('Harris edge detection', img)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
from myfuncs import *

# image1 = cv2.imread("/test_images/misc/TEST_SUB.jpg")
# image2 = cv2.imread("/test_images/misc/TEST_SUB_2.jpg")
# image3 = cv2.subtract(image2, image1)
# cv2.imwrite("test_images/misc/Subtract test.jpg", image3)

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame', fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
