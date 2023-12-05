import cv2 as cv

img = cv.imread('imgs/beach.jpg')

cv.imshow('Beach', img)

# Converting to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur 

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# Dilating the image

dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilate", dilate)

# Eroding

eroded = cv.erode(dilate, (7,7), iterations=3)
cv.imshow("Eroded", eroded)


# Resize 

resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resize)

# Cropping

cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)
cv.destroyAllWindows()