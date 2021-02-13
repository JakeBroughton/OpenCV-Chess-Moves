# import cv2
#
# # load images
# oneimage = cv2.imread('test_images/misc/Difference_Test_003.jpg')
# twoimage = cv2.imread('test_images/misc/Difference_Test_002.jpg')
# threeimage = cv2.imread('test_images/misc/Difference_Test_001.jpg')
#
#
# diffy1 = cv2.subtract(oneimage, twoimage)
#
# diffy2 = cv2.subtract(twoimage, threeimage)
#
# diffy3 = cv2.subtract(diffy2, diffy1)
#
# cv2.imshow("Difference", diffy1)
#
# cv2.waitKey(0)



# image2 = cv2.imread("/test_images/misc/TEST_SUB_2.JPG")

# compute difference
# difference = cv2.subtract(image1, image2)

# Display image
# cv2.imshow("difference", image1)
#
# import cv2
# from myfuncs import *
#
# cv2.imshow('Harris edge detection', img)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
#
#
# from myfuncs import *
# print(squarename())
# =======
# cameracheck(0)

# import cv2
# import numpy as np
# from myfuncs import *
# h, w = 480, 480

# image1 = cv2.imread("test_images/real_board.jpg")
# image1 = cv2.resize(image1, (h,w))
#
# image2 = cv2.imread("test_images/real_board_2.jpg")
# image2 = cv2.resize(image2, (h,w))
#
# image3 = cv2.imread('test_images/empty_real_board.jpg')
# image3 = cv2.resize(image3, (h,w))
#
# bigwindow([image1, image2, image3], [h, w])
#
# cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# image1 = np.zeros((w, h))
# image1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# image3 = np.zeros((w, h))
# image3 = cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY)
# while True:
#     ret, rawSource = cap.read()
#     image2 = rawSource
#     image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#     bigwindow([image1, image2, image3], (h, w))
#     cv2.waitKey(1)

import cv2
import numpy as np
h, w = 480, 480


def bigwindow(windows, size, title):
    wcount = 0
    newwindows = []
    for w in windows:
        w = cv2.resize(w, size)
        newwindows.append(w)
        wcount += 1
    if len(windows) == 4:
        hconcat1 = cv2.hconcat([newwindows[0], newwindows[1]])
        hconcat2 = cv2.hconcat([newwindows[2], newwindows[3]])

    newconcat = cv2.vconcat([hconcat1, hconcat2])
    cv2.imshow(title, newconcat)


def create_blank(width, height, rgb_color=(0, 0, 0)):
    # Create blank openCV image

    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color

    return image


image1 = cv2.imread("test_images/real_board.jpg")
image1 = cv2.resize(image1, (h,w))

image2 = create_blank(w, h)
# cv2.imshow("image2", image2)
concat = cv2.hconcat([image1, image2])
cv2.imshow("Blank Concat Test", concat)
cv2.waitKey(0)
