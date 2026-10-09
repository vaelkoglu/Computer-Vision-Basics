import cv2 as cv
import numpy as np

# note: to know the type of the image use : print (type(ANYTHING))

# Define the folder path where the image is located
path = "create_image/"

# Load the image from the path into a NumPy array (matrix)
img = cv.imread(path +"img.png")

# Create a resizable window with auto-size property
cv.namedWindow("create_image" , cv.WINDOW_AUTOSIZE)

# Display the loaded image inside the window
cv.imshow("create_image",img)

# Wait indefinitely until the user presses any keyboard key
cv.waitKey(0)


# Create a deep copy of the image (independent copy in memory)
m1 = np.copy(img)

# Assign the original image reference to m2 (any change to img will affect m2)
m2 = img

# Check the data type of the image object
type(img)

# Modify a specific Region of Interest (ROI) pixels: rows 100 to 200, columns 200 to 300, all channels (:) set to value 100
img [100:200,200:300, :] = 100

# Display m2 to show how reference assignment works (changes in img reflect in m2)
cv.imshow ("m2" ,m2)

# Wait for a key press
cv.waitKey(0)

# Create a blank (black) image/matrix of size 550x700 with 8-bit unsigned integer type (uint8)
m3 = np.zeros([550,700] , np.uint8)

# Display the blank matrix m3
cv.imshow("m3",m3)

# Wait for a key press
cv.waitKey(0)

# Create another blank matrix of size 512x512 with uint8 type
m4 = np.zeros([512,512] , np.uint8)

# Display the blank matrix m4
cv.imshow("m4",m4)

# Wait for a key press
cv.waitKey(0)

# Clean up and close all active OpenCV display windows
cv.destroyAllWindows()



