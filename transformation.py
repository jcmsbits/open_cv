import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Parque', img)

# Si x es positivo, la imagen se mueve hacia la derecha
# Si x es negativo, la imagen se mueve hacia la izquierda
# Si y es positivo, la imagen se mueve hacia abajo
# Si y es negativo, la imagen se mueve hacia arriba

def translate(img, x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    #print(transMat)

    # Dimensions es el tamano que queremos que traslade de la imagen
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)


translated_img = translate(img, 100, 100) 

cv.imshow('Imagen trasladada',translated_img)

# Rotation

# Si el parametro angle es positivo, la rotacion se hara 
# en sentido contrario del reloj
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    # rotPoint es el Eje o punto desde el cual se va a rotar
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    dimensions = (width, height)
    
    # Escale en getRotationMatrix2D me hace un zoom en la imagen
    rotMat = cv.getRotationMatrix2D(rotPoint, angle,1.0)
    
    return cv.warpAffine(img, rotMat, dimensions)

rotate_img = rotate(img, 45)
cv.imshow('Imagen rotada',rotate_img)

# Al rotar por 2da vez la imagen, se obtiene una imagen recortada
# Producto de la rotacion anterior
rotated_img = rotate(rotate_img, 45)
cv.imshow('Imagen rotada 2 veces',rotated_img)

img_90 = rotate(img, 90)
cv.imshow('Imagen rotada 90 grados',img_90)

# Cambiando el tamano de la imagen

resized_img =  cv.resize(img, (400,400), interpolation=cv.INTER_AREA)
cv.imshow('Imagen redimensionada', resized_img)

# Girando la imagen con flip

#Imagen girada verticalmente con eje horizontal
flip_vertical_img = cv.flip(img,0)
cv.imshow('Imagen girada verticalmente', flip_vertical_img)

# Imagen rotada horizontalmente con eje vertical
flip_horizontal_img = cv.flip(img,1)
cv.imshow('Imagen girada horizontalmente', flip_horizontal_img)

#Imagen rotada tanto vertical como horizontalmente
flip_vertical_and_horizontal_img = cv.flip(img,-1)
cv.imshow('Imagen girada', flip_vertical_and_horizontal_img)

# Cropping o recortando

cropped = img[200:400,300:400]
cv.imshow('Recortada o Cropped Image',cropped)

cv.waitKey(0)