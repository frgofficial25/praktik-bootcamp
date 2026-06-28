import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('D:/UB/FRG/Bootcamp/bootcamp_cv/KelasDasar/2_OpenCV/Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, (255, 255, 255), thickness=-1)
cv.imshow('Circle', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

# Grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure(1)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])

# Colour histogram
colour_mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Colour Mask', colour_mask)

plt.figure(2)
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors) :
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)