import cv2 as cv
import numpy as np

img = cv.imread('imgs/beach.jpg')
cv.imshow('Beach', img)

# Split the image

b, g, r = cv.split(img)
cv.imshow("BLUE", b)
cv.imshow("GREEN", g)
cv.imshow("RED", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


# Merge the images

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
cv.destroyAllWindows()