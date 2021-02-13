import numpy as np
import cv2


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
        return True
