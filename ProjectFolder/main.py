from myfuncs import *
import cv2
import numpy as np

# Parameters
windowH, windowW = 480, 480

circles = np.zeros((4, 2), np.int)

counter = 0


def mousepoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDBLCLK:
        circles[counter] = x, y
        counter += 1
        # print(circles)


# Load base test image, to be later changed to a video source #
# filename = 'test_images/blank_board.jpg'
filename = 'test_images/alex_before.jpg'
source = cv2.imread(filename)

cornerClick = cv2.resize(source, (windowH, windowW))
cv2.imshow("CornerClick", cornerClick)

base = cornerClick.copy()

cv2.imshow("CornerClick", cornerClick)


print("Double click corners of board.")

while True:
    if counter == 4:
        # TODO: use myfuncs.py to sort corners into correct order (top left, top right, bottom left .etc)
        order(circles)
        # Warp image perspective #
        pos1 = np.float32(order(circles))
        pos2 = np.float32([[0, 0], [windowW, 0], [0, windowH], [windowW, windowH]])
        matrix = cv2.getPerspectiveTransform(pos1, pos2)
        imgOutput = cv2.warpPerspective(base, matrix, (windowW, windowH))
        break

    for x in range(0, 4):
        cv2.circle(cornerClick, (circles[x][0], circles[x][1]), 5, (0, 255, 0), cv2.FILLED)
    cv2.imshow("CornerClick", cornerClick)
    # Look for double clicks on "base" window
    cv2.setMouseCallback('CornerClick', mousepoints)
    cv2.waitKey(1)
cv2.destroyWindow("CornerClick")
cv2.imshow("Fixed Perspective", imgOutput)
individualSquareMatrix = splitboard(imgOutput)
print(len(individualSquareMatrix))
cv2.imshow("test", individualSquareMatrix[0])
cv2.imwrite("test_images/BeforeSquare0.jpg", individualSquareMatrix[0])

# Decide if square contains a piece or not
# boardSquare = test[0]
# boardGrey = cv2.cvtColor(boardSquare, cv2.COLOR_BGR2GRAY)
# boardEdges = cv2.Canny(boardGrey, 50, 200)


cv2.waitKey(0)

# Split board into grid #
