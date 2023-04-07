import cv2 as cv
path='C:/Users/ither/OneDrive/Desktop/test.jpeg'
img = cv.imread(path)
cv.imshow('Test', img)
cv.waitKey(0)
