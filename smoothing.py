import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')   


# Average

ave_img = cv.blur(img, (3,3))
cv.imshow('Imagen Difuminada', ave_img)
 
# Gaussian Blur 
# Gaussian es menos fuerte que blur
# 3er argumento es la desviacion estandar del eje x
gauss = cv.GaussianBlur(img, (7,7),0)
cv.imshow('Imagen con Gaussian', gauss)

# Median Blur
# Toma la media del conjunto de pixel que hay que alrededor del 
# Medio del kernel y lo cambia

median = cv.medianBlur(img, 3)
cv.imshow('Imagen con la mediana', median)

# Bilateral

bilateral = cv.bilateralFilter(img, 10, 35 ,25 )
cv.imshow('Imagen bilateral', bilateral)


cv.waitKey(0)
#ave_img = cv.GaussianBlur()