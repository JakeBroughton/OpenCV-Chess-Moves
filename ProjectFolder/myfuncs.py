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


# TODO: make function to split board up into individual squares
def splitboard():
    pass

