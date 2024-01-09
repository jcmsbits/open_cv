import cv2 as cv

#img = cv.imread('./Resources/Photos/lady.jpg')
img = cv.imread('./Resources/Photos/group 1.jpg')
#cv.imshow('Person', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('./haar_face.xml')

# Cambiando el numero de minNeighbors aumenta la precisión
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

# CascadeClassifier devuelve la cantidad de rostros que encontro
# en una lista de tuplas, con el ancho y alto dentro de la imagen
print(f'Number of faces found {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=1)

cv.imshow('Faces Recognize', img)

cv.waitKey(0)