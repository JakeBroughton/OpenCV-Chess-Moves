from myfuncs import *
import cv2
import numpy as np

# Parameters
windowH, windowW = 450, 450

circles = np.zeros((4, 2), np.int)

counter = 0


def mousepoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDBLCLK:
        circles[counter] = x, y
        counter += 1
        print(circles)


# Load base test image, to be later changed to a video source #
# filename = 'test_images/blank_board.jpg'
filename = 'test_images/real_board_2.jpg'
source = cv2.imread(filename)


cornerClick = cv2.resize(source, (windowH, windowW))
cv2.imshow("CornerClick", cornerClick)

base = cornerClick.copy()


cv2.imshow("CornerClick", cornerClick)


print("Double click corners of board.")

while True:
    if counter == 4:
        # TODO: use myfuncs.py to sort corners into correct order (top left, top right, bottom left .etc)

        # Warp image perspective #
        pos1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pos2 = np.float32([[0, windowH], [windowW, windowH], [0, 0], [windowW, 0]])
        matrix = cv2.getPerspectiveTransform(pos1, pos2)
        imgOutput = cv2.warpPerspective(base, matrix, (windowW, windowH))
        break

    for x in range(0, 4):
        cv2.circle(cornerClick, (circles[x][0], circles[x][1]), 5, (0, 255, 0), cv2.FILLED)
    cv2.imshow("CornerClick", cornerClick)
    # Look for double clicks on "base" window

    cv2.setMouseCallback('CornerClick', mousepoints)

    cv2.waitKey(1)

cv2.imshow("Fixed Perspective", imgOutput)
cv2.waitKey(0)

# Split board into grid #

# Close all windows on ESC key

# Test change
test = True
