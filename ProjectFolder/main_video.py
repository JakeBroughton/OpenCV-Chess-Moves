# Imports
from myfuncs import *
import cv2
import numpy as np

# Parameters
windowH, windowW = 480, 480
circles = np.zeros((4, 2), np.int)
counter = 0

cameraID = 0

filename = 'test_images/alex_nocamera.jpg'
cap = cv2.VideoCapture(cameraID)

font = cv2.FONT_HERSHEY_SIMPLEX

cap_count = 0

# Check camera has access
if cameracheck(cameraID):
    pass
else:
    raise SystemExit


# Mouse click function
def mousepoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDBLCLK:
        circles[counter] = x, y
        counter += 1
        # print(circles)


# TODO: implement error handling for camera not plugged in
# Click corners and warp perspective
while True:
    ret, rawSource = cap.read()
    rawSource = cv2.resize(rawSource, (windowW, windowH))
    cv2.imshow('Raw Source', rawSource)

    cv2.putText(rawSource,
                'Double-click corners',
                (50, 50),
                font, 1,
                (0, 255, 255),
                2,
                cv2.LINE_4)

    if counter == 4:
        # TODO: use myfuncs.py to sort corners into correct order (top left, top right, bottom left .etc)
        order(circles)
        # Warp image perspective #
        pos1 = np.float32(order(circles))
        pos2 = np.float32([[0, 0], [windowW, 0], [0, windowH], [windowW, windowH]])
        matrix = cv2.getPerspectiveTransform(pos1, pos2)
        correctedImage = cv2.warpPerspective(rawSource, matrix, (windowW, windowH))
        cv2.destroyWindow("Raw Source")
        break

    for x in range(0, 4):
        cv2.circle(rawSource, (circles[x][0], circles[x][1]), 5, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Raw Source", rawSource)
    # Look for double clicks on "base" window
    cv2.setMouseCallback('Raw Source', mousepoints)
    cv2.waitKey(1)

# Stream corrected footage
while True:
    ret, rawSource = cap.read()
    rawSource = cv2.resize(rawSource, (windowW, windowH))
    correctedImage = cv2.warpPerspective(rawSource, matrix, (windowW, windowH))
    cv2.imshow("Corrected Perspective", correctedImage)

    k = cv2.waitKey(33)
    if k == 32:  # Space key
        cap_filename = "test_images/misc/cap_count" + str(cap_count) + ".jpg"
        cv2.imwrite(cap_filename, correctedImage)
        cap_count += 1
        print(cap_count)
    if k == 93:  # Right square bracket
        individuals = splitboard(correctedImage)
        cv2.imshow("test", individuals[0])
    if k == 27:  # Escape key
        break
    elif k == -1:
        continue
    else:
        print(k)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
