#image Pseudo Color Enhancement
import cv2 as cv


img = cv.imread("img.png")
img1 = cv.imread("img1.png")

#load image
#be careful about the win-name should be same at each operation
cv.namedWindow("test_color", cv.WINDOW_AUTOSIZE)
cv.imshow ("test_color" , img)
cv.waitKey(0)


cv.namedWindow ("test1_color" , cv.WINDOW_AUTOSIZE)
cv.imshow("test1_color" , img1)
cv.waitKey(0)



#Apply-Color-Map by using the blew

#COLORMAP_AUTUMN
#COLORMAP_BONE
#COLORMAP_WINTER
#COLORMAP_OCEAN
#COLORMAP_PINK
#COLORMAP_COOL
#COLORMAP_JET  -- here some color that you can use
dst = cv.applyColorMap(img,cv.COLORMAP_SUMMER)
cv.imshow("output" , dst)
cv.waitKey(0)
cv.destroyWindow("output")