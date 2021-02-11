from myfuncs import *
import cv2
import numpy as np

# Parameters
windowH = 450
windowW = 450

x_squares = 8
y_squares = 7

x_no = x_squares - 1
y_no = y_squares - 1

# Load base test image, to be later changed to a video source #
#filename = 'test_images/blank_board.jpg'
filename = 'test_images/calibration.jpg'

source = cv2.imread(filename)
# cv2.imshow("Base Image", source)

base = cv2.resize(source, (windowH, windowW))
cv2.imshow("Resize", base)

# Find contours of image and draw #
gray = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)

# Find chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (x_no, y_no), None)
if ret:
    print("Found corners")
    cv2.drawChessboardCorners(gray, (7,6), corners, ret)
    cv2.imshow("image", gray)

    print(type(corners))
    print(len(corners))
    print(corners)
# Warp image perspective #

# Split board into grid #

# Wait for ESC key
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()


