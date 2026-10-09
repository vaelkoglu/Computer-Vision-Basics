#How can we convert the RGB image to Gray let see
import cv2 as cv

#first we have to read the path of image

img = cv.imread("img.png")
cv.namedWindow("Test_image",cv.WINDOW_AUTOSIZE)
cv.imshow("Test_image" , img)
cv.waitKey(0)


#converting the image color to gray
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.namedWindow("Gray_image" , cv.WINDOW_AUTOSIZE)
cv.imshow ("Gray_image" , gray)
cv.waitKey(0)



#also we can convert it as

img1 = cv.imread("img1.png", cv.IMREAD_GRAYSCALE)
cv.namedWindow("Gray_imge1", cv.WINDOW_AUTOSIZE)
cv.imshow("Gray_imge1", img1)
cv.waitKey(0)


cv.destroyAllWindows()
