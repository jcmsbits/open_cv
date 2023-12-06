import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats 2.jpg')

# Para hacer la mascara la imagen superpuesta debe tener
# La misma dimension que la imagen original
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (105,70), (265,250), 255, -1)

masked_img = cv.bitwise_and(img,img,mask=rectangle)
#masked_img = cv.bitwise_and(img,img,mask=circle)

cv.imshow('Imagen enmascarada', masked_img )

cv.waitKey(0)