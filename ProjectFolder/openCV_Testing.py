import cv2

# load images
oneimage = cv2.imread('test_images/misc/Difference_Test_003.jpg')
twoimage = cv2.imread('test_images/misc/Difference_Test_002.jpg')
threeimage = cv2.imread('test_images/misc/Difference_Test_001.jpg')


diffy1 = cv2.subtract(oneimage, twoimage)
diffy2 = cv2.subtract(twoimage, threeimage)

diffy3 = cv2.subtract(diffy2, diffy1)

cv2.imshow("Difference", diffy1)

cv2.waitKey(0)
#image2 = cv2.imread("/test_images/misc/TEST_SUB_2.JPG")

# compute difference
#difference = cv2.subtract(image1, image2)

# Display image
#cv2.imshow("difference", image1)
