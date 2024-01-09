import cv2 as cv
import numpy as np

#img = cv.imread('./Resources/Photos/cats.jpg')
img = cv.imread('./Resources/Photos/park.jpg')

cv.imshow('Cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)

# Con convertScaleAbs nos ahorramos el np.unit8(np.absolute(lap))
lap_img = cv.convertScaleAbs(lap)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)
cv.imshow('Another Laplacian', lap_img)


# Sobel
sobelx = cv.Sobel(gray,cv.CV_64F, 1, 0)
cv.imshow('Sobel X', sobelx)
sobely = cv.Sobel(gray,cv.CV_64F, 0, 1)
cv.imshow('Sobel Y', sobely)

# Uniendo con bitwise Sobel X y Sobel Y

bit_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X and Y', bit_sobel)

# Comparando con Canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)
