import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('imgs/beach.jpg')
cv.imshow('Beach', img)

# Averaging

average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian Blur

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur

median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral) 

cv.waitKey(0)
cv.destroyAllWindows()