import cv2 as cv

img = cv.imread('D:/UB/FRG/Bootcamp/bootcamp_cv/KelasDasar/2_OpenCV/Resources/Photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('D:/UB/FRG/Bootcamp/bootcamp_cv/KelasDasar/2_OpenCV/Resources/Videos/dog.mp4')
isTrue, frame = capture.read()

while isTrue :
    cv.imshow('Video', frame)
    isTrue, frame = capture.read()
    if cv.waitKey(20) & 0xFF==ord('d') :
        break

capture.release()
cv.destroyAllWindows()