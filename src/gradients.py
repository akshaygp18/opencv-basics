import cv2 as cv
import numpy as np

img = cv.imread('imgs/beach.jpg')
cv.imshow('Beach', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Lapalacian

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)





cv.waitKey(0)
cv.destroyAllWindows()