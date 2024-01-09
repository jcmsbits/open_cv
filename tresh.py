import cv2 as cv

img = cv.imread('./Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cats', gray)

# Simple Thresholding

threshold,tresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Imagen Binaria', tresh)

# Con THRESH__BINARY_INV se invierte los valores, los mayores a 0
# y los menores a maxvalue
threshold_inv,tresh_inv = cv.threshold(gray, 125,255, cv.THRESH_BINARY_INV) 
cv.imshow('Inversa Binaria', tresh_inv)

# Adaptative Tresholding
# Se tiene que pasar una imagen en escala de grises
# Con adaptative el define los valores que se van a cambiar
# a diferencia con threshold que se especifica la cantidad
# minima que se va a cambiar por un maxvalue

#Adaptative tiene MEAN y Gaussian
# Con Gaussian se obtiene mejores imagenes

# adaptive_tresh = cv.adaptiveThreshold(gray,255, 
#                                       cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,
#                                       11,9)
adaptive_tresh = cv.adaptiveThreshold(gray,255, 
                                      cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,
                                      3,3)

cv.imshow('Adaptative Tresholding', adaptive_tresh)

cv.waitKey(0)