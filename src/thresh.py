import cv2 as cv
import numpy as np

img = cv.imread('imgs/beach.jpg')
cv.imshow('Beach', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inv', thresh_inv)


# Adaptive thresholding 

adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11,3)
cv.imshow('Adaptive Threshold', adaptive_threshold)

cv.waitKey(0)
cv.destroyAllWindows()