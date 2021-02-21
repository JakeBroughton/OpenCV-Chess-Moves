# Imports
from myfuncs import *
import cv2
import numpy as np
from datetime import datetime
import ctypes

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
    print(f'Camera found at id {cameraID}.')
    pass
else:
    print(f'Could not find camera with ID {cameraID}.')
    raise SystemExit


# Mouse click function
def mousepoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDBLCLK:
        circles[counter] = x, y
        counter += 1
        # print(circles)


# Click corners and warp perspective
while True:
    ret, rawSource = cap.read()
    rawSource = cv2.resize(rawSource, (windowW, windowH))
    cv2.imshow('Raw Source', rawSource)

    windowtext(rawSource, "Double click corners")

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

    for i in range(0, 4):
        cv2.circle(rawSource, (circles[i][0], circles[i][1]), 5, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Raw Source", rawSource)
    # Look for double clicks on "base" window
    cv2.setMouseCallback('Raw Source', mousepoints)
    cv2.waitKey(1)

# Stream corrected footage
# Create empty images for current and previous frames
ret, rawSource = cap.read()
rawSource = cv2.resize(rawSource, (windowW, windowH))
currentFrame = create_blank(windowW, windowH)
previousFrame = currentFrame

# currentFrame = np.zeros((windowW, windowH))
# previousFrame = np.zeros((windowW, windowH))

# print("Keybinds: \n [ - End of turn \n space - save current view to file \n ] - show square 0 in window")
ctypes.windll.user32.MessageBoxW(0, "Keybinds: \n "
                                    "\t [ \t - \t save snapshot \n "
                                    "\t Space \t - \t End of turn \n"
                                    "\t ] \t - \t show square 0 in window \n"
                                    "\t ESC \t - \t Exit", "Keybinds", 1)

turn_count = -2;
print("Press space twice to initialise system.")
while True:
    ret, rawSource = cap.read()
    rawSource = cv2.resize(rawSource, (windowW, windowH))
    correctedImage = cv2.warpPerspective(rawSource, matrix, (windowW, windowH))

    # Piece that moved difference
    before_move_diff = difference(currentFrame, previousFrame)

    # Location that the piece moved to difference
    after_move_diff = otherdifference(currentFrame, previousFrame)

    bigwindow([correctedImage, previousFrame, currentFrame,
               before_move_diff, after_move_diff], (windowW, windowH), "LegGambit")

    # cv2.imshow("Process this fucking image", after_move_diff)
    findsquares(before_move_diff, after_move_diff, turn_count)

    k = cv2.waitKey(33)
    if k == 91:  # Left square bracket
        cap_filename = "test_images/misc/cap_count" + str(cap_count) + ".jpg"
        cv2.imwrite(cap_filename, correctedImage)
        cap_count += 1
        print(cap_count)
    if k == 93:  # Right square bracket
        individuals = splitboard(correctedImage)
        cv2.imshow("test", individuals[0])[[]]
    if k == 32:  # Spacekey

        previousFrame = currentFrame
        currentFrame = correctedImage
        turn_count += 1
        print(turn_count)
        pass
    if k == 27:  # Escape key
        break
    elif k == -1:
        continue
    else:
        # print(k)
        pass


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
