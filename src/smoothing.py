import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('imgs/beach.jpg')
cv.imshow('Beach', img)

# Averaging

average = cv.blur(img, (3,3))
cv.imshow('Average', average)



cv.waitKey(0)
cv.destroyAllWindows()