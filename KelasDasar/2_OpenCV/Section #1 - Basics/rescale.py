import cv2 as cv

# Work for Images, Videos, and Live Video
def rescale_frame(frame, scale=0.75) :
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) # INTER_AREA : downscaling, INTER_LINEAR : downscaling or upscaling, INTER_CUBIC : upscaling

# Only Work for Live Video
def changeRes(capture, width, height) :
    capture.set(3, width)
    capture.set(4, height)

img = cv.imread('D:/UB/FRG/Bootcamp/bootcamp_cv/KelasDasar/2_OpenCV/Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)
cv.waitKey(0)

img_resize = rescale_frame(img, .2)
cv.imshow('Cat_resize', img_resize)
cv.waitKey(0)

capture = cv.VideoCapture('D:/UB/FRG/Bootcamp/bootcamp_cv/KelasDasar/2_OpenCV/Resources/Videos/dog.mp4')
isTrue, frame = capture.read()

while isTrue :
    frame_resize = rescale_frame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resize)
    isTrue, frame = capture.read()
    if cv.waitKey(20) & 0xFF==ord('d') :
        break

capture.release()
cv.destroyAllWindows()

camera = cv.VideoCapture(0)
changeRes(camera, 100, 200)
isTrue, frame = camera.read()

while isTrue :
    cv.imshow('Camera', frame)
    isTrue, frame = camera.read()
    if cv.waitKey(20) & 0xFF==ord('d') :
        break

camera.release()
cv.destroyAllWindows()