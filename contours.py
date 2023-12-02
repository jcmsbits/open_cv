import cv2 as cv
import numpy as np
# Contornos(Contours)

img = cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype=np.uint8)


gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray_img)

blur = cv.GaussianBlur(gray_img, (5,5),cv.BORDER_DEFAULT)
cv.imshow('Imagen Difuminada', blur)

canny = cv.Canny(blur, 125,175)
cv.imshow('Bordes de la imagen', canny)

# findCountours busca y retorna la cantidad de contornos que tiene la imagen
# La variable countours es una lista de todos los contornos encontrados
# La variable hierarchies contiene la jerarquia de los contornos (adentro de otro, etc)

# cv.CHAIN_APPROX_NONE si no queremos aproximar los contornos, no hace nada
#contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#print(f'{len(contours)} countour(s) found!')
# cv.CHAIN_APPROX_SIMPLE toma los puntos de los contornos cercanos y los une
#contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#print(f'{len(contours)} countour(s) found!')
# cv.RETR_EXTERNAL Regresa todos los contornos afuera
# contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

# cv.RETR_TREE devuelve todos los contornos jerarquicos
#contours, hierarchies = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
#print(f'{len(contours)} countour(s) found!')

#Hay otra forma de encontrar contornos, y se llama threshold

# ret, thresh = cv.threshold(gray_img,125,255,cv.THRESH_BINARY)
# cv.imshow('Thresh',thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} countour(s) found!')

# DrawCountour permite dibujar los contornos en una matriz en blanco
# El tercer argumento define la cantidad de contornos a dibujar 
# -1 Selecciona a todos los contornos
# El 4to argumento es el color y el 5to el grosor de las lineas
cv.drawContours(blank, contours,-1, (0,0,255),1)
cv.imshow('Countours Draw', blank)

cv.waitKey(0)