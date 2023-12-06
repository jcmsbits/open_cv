import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
blank = np.zeros(img.shape[:2],dtype = 'uint8')

# Con el metodo split dividimos la imagenes en los 3 colores BGR
b,g,r = cv.split(img)


cv.imshow('Parque', img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Read', r)

# Las matrices de cada color tienen la misma dimension que la imagen original
# La imagenes se ven grises cada una, y en dependencia de su intensidad
# Define que tan fuerte es ese color que predomina en la imagen
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Para ver el color de cada matriz se hace un merge con 2 matrices en blanco
blue_img = cv.merge([b, blank,blank])
green_img = cv.merge([blank, g,blank])
red_img = cv.merge([blank, blank,r])

cv.imshow('Azul', blue_img)
cv.imshow('Verde', green_img)
cv.imshow('Rojo', red_img)

# Para recuperar la imagen, se unen los colores otra vez con merge
merge_img = cv.merge([b,g,r])
cv.imshow('Imagen Fusionada', merge_img)


cv.waitKey(0)