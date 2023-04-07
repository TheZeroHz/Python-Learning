import cv2 as cv

def resize_frame(frame,scale):
    height=int(frame.shape[0] * scale)
    width=int(frame.shape[1] * scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

path='C:/Users/ither/OneDrive/Desktop/test.jpeg'
img = cv.imread(path)
resized_image=resize_frame(img,0.75)
cv.imshow('Original', img)
cv.imshow('Resized', resized_image)
cv.waitKey(0)
