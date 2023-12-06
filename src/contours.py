import cv2 as cv

img = cv.imread('imgs/beach.jpg')

cv.imshow('Beach', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Threshold',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')










cv.waitKey(0)
cv.destroyAllWindows()