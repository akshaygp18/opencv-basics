import cv2 as cv
import numpy as np

img = cv.imread('imgs/person1.jpg')
cv.imshow('Person1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person2', gray)


haar_cascade = cv.CascadeClassifier('D:\Ineuron\opencv-basics\src\haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv.imshow('Detected faces', img)
cv.waitKey(0)
cv.destroyAllWindows()