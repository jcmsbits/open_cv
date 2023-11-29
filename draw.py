import cv2 as cv
import numpy as np

#Creando una imagen en blanco
blank = np.zeros((500,500,3), dtype='uint8')


img = cv.imread('./Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# 1. Paint the image a certain colour
#blank[200:300,300:400] = 0,0,255
#cv.imshow('Blank', blank)
#print(blank[:])

# 2. Dibujando un rectangulo

#rectangule =cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)
# Pintando el rectangulo por dentro con el cv.FILLED o -1
#rectangule =cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#rectangule =cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=-1)

"""Los metodos rectangle y circle modifican la imagen original """
#rectangule =cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangule', blank)

# 3. Dibujando un circulo
#cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255), thickness=3)
# #Se puede rellenar el circulo con -1
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255), thickness=-1)
cv.imshow('Circle',blank)

# 4. Dibujando una linea
# cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,255,255),thickness=2)
# cv.imshow('Linea',blank)

# cv.line(blank,(100,250),(300,400),(255,255,255),thickness=1)
# cv.imshow('Otra Linea',blank)

# Escribir texto

cv.putText(blank, 'Prueba de texto', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.3, (0,255,255), thickness=1, lineType=1)
cv.imshow('Texto', blank)

cv.waitKey(0)