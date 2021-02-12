# TODO: make function that finds top left, top right, bottom left, bottom right coords from list
import numpy as np
from scipy.spatial import distance as dist


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


# TODO: make function to split board up into 64 individual squares
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
    return square
