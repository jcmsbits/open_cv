import cv2 as cv
import numpy as np


blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND
# Muestra lo que se intersecta entre las 2 imagenes
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('BitWise AND (Interseccion)',bitwise_and)

# Bitwise OR
# Muestra lo que contiene las 2 imagenes
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR (Basicamente las superpone)', bitwise_or)

# Bitwise XOR
# Muestra lo que no tiene interseccion entre las 2 imagenes
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR (La no intereseccion en las imagenes)', bitwise_xor)

# Bitwise NOT
# Invierte los colores
rectangle_bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT (Invierte los colores)', rectangle_bitwise_not)

circle_bitwise_not = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT (Invierte los colores)', circle_bitwise_not)



cv.waitKey(0)