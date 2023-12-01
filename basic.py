import cv2 as cv

# Algunas funciones populares de Open_CV

#img = cv.imread('Resources/Photos/cat.jpg')
img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

#Convirtiendo a escala de grises

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Lady Gris',gray)

# Difuminando(desenfocando) la imagen (Blur)

#blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# Para incrementar el desenfoque se incrementa el kernel size
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Desenfoque', blur)

# Borde Cascada(Edge Cascade)

# Con los parametros de threshold se puede reducir los bordes
#canny = cv.Canny(img,100, 105)
# Haciendo el borde de cascada con imagen desenfocada para reducir los bordes
canny = cv.Canny(img,100, 105)
cv.imshow('Borde Cascada', canny)

# Dilatando imagen (Dilating the image)
# Recibe una imagen de bordes como parametros
# A mayor iteracion mas se nota los bordes los bordes
dilated = cv.dilate(canny,(3,3), iterations=1)
cv.imshow('Imagen Dilatada', dilated)

# Erosionando (Eroding)
# Se puede obtener de nuevo la imagen que se dilato

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Erosionado', eroded)

# Cambiando de tamano a la imagen

# interpolation = cv.INTER_CUBIC es mas bueno 
# a la hora de subir el tama;o a la imagen
#resized = cv.resize(img,(1024,720), interpolation=cv.INTER_CUBIC)
resized = cv.resize(img,(1024,720), interpolation=cv.INTER_LINEAR)
cv.imshow('Cambio de tamano', resized)

# Imagen recortada (Cropped)

cropped_img = img[50:200, 30:180]
cv.imshow('Imagen Recortada', cropped_img)

cv.waitKey(0)