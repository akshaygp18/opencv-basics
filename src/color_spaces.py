import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('imgs/beach.jpg')
cv.imshow('Beach', img)


# plt.imshow(img)
# plt.show()

# BGR to grayscale image

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale', gray)

# BGR to hsv image

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab) 

# BGR to RGB image

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)



cv.waitKey(0)
cv.destroyAllWindows()