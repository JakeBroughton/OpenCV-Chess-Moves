import numpy as np
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX


def order(pts):
    # Sort coordinates
    # print("Organizing co-ordinates")
    # print(pts)
    # Sort x coords
    x_sorted = sorted(pts, key=lambda x: x[0])
    # print(x_sorted)

    # Find leftmost and rightmost co-ordinates
    leftmost = x_sorted[:2]
    rightmost = x_sorted[2:]
    # print(leftmost)

    # Sort leftmost by y co-ordinates to find top left and bottom left
    tl, bl = sorted(leftmost, key=lambda x: x[1])
    # print(tl, bl)

    # Sort rightmost by y co-ordinates to find top left and bottom left
    tr, br = sorted(rightmost, key=lambda x: x[1])
    # print(tr, br)
    return tl, tr, bl, br


def splitboard(img):
    squares = []
    col = np.hsplit(img, 8)
    for i in col:
        row = np.vsplit(i, 8)
        for n in row:
            squares.append(n)
    return squares


def squarename(square):
    # return actual square name, given location in individualSquareMatrix
    BoardCoord = [
    "h8",
    "g8",
    "f8",
    "e8",
    "d8",
    "c8",
    "b8",
    "a8",
    "h7",
    "g7",
    "f7",
    "e7",
    "d7",
    "c7",
    "b7",
    "a7",
    "h6",
    "g6",
    "f6",
    "e6",
    "d6",
    "c6",
    "b6",
    "a6",
    "h5",
    "g5",
    "f5",
    "e5",
    "d5",
    "c5",
    "b5",
    "a5",
    "h4",
    "g4",
    "f4",
    "e4",
    "d4",
    "c4",
    "b4",
    "a4",
    "h3",
    "g3",
    "f3",
    "e3",
    "d3",
    "c3",
    "b3",
    "a3",
    "h2",
    "g2",
    "f2",
    "e2",
    "d2",
    "c2",
    "b2",
    "a2",
    "h1",
    "g1",
    "f1",
    "e1",
    "d1",
    "c1",
    "b1",
    "a1",
    ]
    return BoardCoord[square]


def cameracheck(camera):
    # Check if specified camera ID is plugged in
    cap = cv2.VideoCapture(camera)
    if cap is None or not cap.isOpened():
        # No camera found at ID position
        return False
    else:
        # Camera found
        cap.release()
        return True


# TODO: Improve function so it can be given different numbers of windows
def bigwindow(windows, size, title):
    # Give function a list of windows to display, shows them all in one big window

    # Input list of windows and display them all
    # wcount = 0
    # newwindows = []
    # for w in windows:
    #     w = cv2.resize(w, size)
    #     newwindows.append(w)
    #     wcount += 1
    #
    # concat = cv2.hconcat(newwindows)
    # cv2.imshow(title, concat)
    wcount = 0
    newwindows = []
    for w in windows:
        w = cv2.resize(w, size)
        newwindows.append(w)
        wcount += 1
    if len(windows) == 4:
        hconcat1 = cv2.hconcat([newwindows[0], newwindows[1]])
        hconcat2 = cv2.hconcat([newwindows[2], newwindows[3]])

    if len(windows) == 5:
        blank = create_blank(480, 480)
        hconcat1 = cv2.hconcat([newwindows[0], newwindows[1], newwindows[2]])
        hconcat2 = cv2.hconcat([newwindows[3], newwindows[4], blank])

    if len(windows) == 6:
        hconcat1 = cv2.hconcat([newwindows[0], newwindows[1], newwindows[2]])
        hconcat2 = cv2.hconcat([newwindows[3], newwindows[4], newwindows[5]])

    concat = cv2.vconcat([hconcat1, hconcat2])
    cv2.imshow(title, concat)


def windowtext(window, text):
    cv2.putText(window,
                str(text),
                (50, 50),
                font, 1,
                (0, 255, 255),
                2,
                cv2.LINE_4)


def difference(img1, img2):
    diffy = cv2.subtract(img1, img2)
    return diffy


def otherdifference(img1, img2):
    otherdiffy = cv2.subtract(img2, img1)
    return otherdiffy


def create_blank(width, height, rgb_color=(0, 0, 0)):
    # Create blank openCV image

    # Create black blank image
    image = np.zeros((height, width, 3), np.uint8)

    # Since OpenCV uses BGR, convert the color first
    color = tuple(reversed(rgb_color))
    # Fill image with color
    image[:] = color
    return image


# TODO: Find coordinates of changed pixels
def findsquares(before, after):


    before_grey = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    before_edges = cv2.Canny(before_grey, 30, 200)

    after_grey = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
    after_edges = cv2.Canny(after_grey, 30, 200)

    b_contours, b_hierarchy = cv2.findContours(before_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    a_contours, a_hierarchy = cv2.findContours(after_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(after_grey, a_contours, -1, (0, 255, 0), 3)
    cv2.drawContours(before_grey, b_contours, -1, (0, 255, 0), 3)

    cv2.imshow("Move location", after_edges)
    cv2.imshow("Piece that Moved", before_edges)

    a_areas = [cv2.contourArea(c) for c in a_contours]
    b_areas = [cv2.contourArea(d) for d in b_contours]

    combo = cv2.add(before_edges, after_edges)

    # if len(a_areas) > 0:
    #     max_a_index = np.argmax(a_areas)
    #     contours = a_contours[max_a_index]
    #     xa, ya, w, h = cv2.boundingRect(contours)
    #     print(f"Found after co-ords: x: {xa}, {ya}")
    #     if len(b_areas) > 0:
    #         max_a_index = np.argmax(b_areas)
    #         contours = b_contours[max_a_index]
    #         xb, yb, w, h = cv2.boundingRect(contours)
    #         print(f"Found before co-ords: x: {xb}, {yb}")
    #         start_point = (xb, yb)
    #         end_point = (xa, ya)
    #         test = create_blank(480, 480)
    #         test = cv2.arrowedLine(test, start_point, end_point, (0, 255, 0), 10)
    #         cv2.imshow("yeet line", test)
    if len(a_areas) > 0:
        max_a_index = np.argmax(a_areas)
        contours = a_contours[max_a_index]
        xa, ya, w, h = cv2.boundingRect(contours)
        print(f"Found after co-ords: x: {xa}, {ya}")
        if len(b_areas) > 0:
            max_a_index = np.argmax(b_areas)
            contours = b_contours[max_a_index]
            xb, yb, w, h = cv2.boundingRect(contours)
            print(f"Found before co-ords: x: {xb}, {yb}")
            start_point = (xb, yb)
            end_point = (xa, ya)
            return start_point, end_point

    else:
        return (0, 0), (0, 0)
