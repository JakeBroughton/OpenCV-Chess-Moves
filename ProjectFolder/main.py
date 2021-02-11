from myfuncs import *
import cv2
import numpy as np

# Parameters
windowH = 450
windowW = 450

# Load base test image, to be later changed to a video source #
filename = 'test_images/empty_real_board_wood.jpg'
source = cv2.imread(filename)
# cv2.imshow("Base Image", source)

base = cv2.resize(source, (windowH, windowW))
cv2.imshow("Resize", base)

# Find contours of image and draw #
baseGrey = cv2.cvtColor(base, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(baseGrey, 200, 255, 0)
cv2.imshow("Threshold", thresh)
# Contours contains list of contours
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# Draw contours
contourDraw = cv2.drawContours(baseGrey, contours, -1, (0, 255, 0), 3)
cv2.imshow("Contours", contourDraw)

# Find largest contour, most likely chess board #

# Warp image perspective #

# Split board into grid #

# Wait for ESC key
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
