# !pip install opencv-python

import cv2 as cv


#reading the path of the image
img = cv.imread ("cat_img.png")

#namedwindow is a function used to create a window object that can be used as a placeholder for displaying images, videos, or UI elements (like trackbars).

cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

#imshow cv2.imshow() is the primary function in OpenCV used to display an image or a video frame inside a graphical window.

cv.imshow("opencv_test" , img)
cv.waitKey(0)
cv.destroyWindow("opencv_test")