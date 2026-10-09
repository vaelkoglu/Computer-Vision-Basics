import cv2 as cv
import numpy as np

src = cv.imread("img.png")
src1 = cv.imread("img1.png")

# Get information about our image like the height, width and channel
h,w,ch = src.shape
h, w, ch = src.shape
print(f"Height: {h}, Width: {w}, Channels: {ch}")
h,w,ch = src1.shape
h, w, ch = src1.shape
print(f"Height: {h}, Width: {w}, Channels: {ch}")

#let the W and H same even if both image are different form each other
src = cv.resize(src1, (w, h))
# add

add_result = np.zeros(src.shape,src1.dtype )
cv.add(src , src1 ,add_result)
cv.imshow ("add",add_result)
cv.waitKey(0)

# subtract
sub_result =np.zeros (src.shape , src1.dtype)
cv.subtract(src ,src1 , sub_result)
cv.imshow ("sub",sub_result)
cv.waitKey(0)

#Multiply
mul_result = np.zeros (src.shape,src1.dtype)
cv.multiply(src , src1 , mul_result)
cv.imshow("mul" , mul_result)
cv.waitKey(0)

#Div
div_result = np.zeros (src.shape , src1.dtype)
cv.divide(src,src1 ,div_result)
cv.imshow ("div",div_result)
cv.waitKey(0)

cv.destroyAllWindows()