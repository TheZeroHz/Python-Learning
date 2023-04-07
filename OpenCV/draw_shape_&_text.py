import cv2 as cv

def resize_frame(frame,scale):
    height=int(frame.shape[0] * scale)
    width=int(frame.shape[1] * scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def avg_cord(origin,endpoint):
    return (int((origin[0]+endpoint[0])/2),int((origin[1]+endpoint[1])/2))

path='C:/Users/ither/OneDrive/Desktop/test.jpeg'
img = cv.imread(path)
image_with_shapes=resize_frame(img,0.75)

RECT_ORIGIN=(40,40)
RECT_ENDPOINT=(144,144)
LINE_ORIGIN=(160,160)
LINE_ENDPOINT=(200,200)
CIRCLE_ORIGIN=(255,255)
CIRCLE_RADIUS=40

cv.rectangle(image_with_shapes,RECT_ORIGIN,RECT_ENDPOINT,(0,0,255),thickness=1)
cv.line(image_with_shapes,LINE_ORIGIN,LINE_ENDPOINT,(0,0,255),thickness=1)
cv.circle(image_with_shapes,CIRCLE_ORIGIN,CIRCLE_RADIUS,(0,0,255),thickness=1)
cv.putText(image_with_shapes,'Rect',avg_cord(RECT_ORIGIN,RECT_ENDPOINT),cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,255),1)
cv.putText(image_with_shapes,'Circle',CIRCLE_ORIGIN,cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,255),1)
cv.putText(image_with_shapes,'Line',avg_cord(LINE_ORIGIN,LINE_ENDPOINT),cv.FONT_HERSHEY_TRIPLEX,0.5,(0,0,255),1)

cv.imshow('Original', img)
cv.imshow('After drawing shapes & Text',image_with_shapes)
cv.waitKey(0)
