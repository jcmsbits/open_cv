import numpy as np
import cv2 as cv
peoples = ['Ben Afflek', 'Elton John','Jerry Seinfield','Madonna','Mindy Kaling']
# Cargando el clasificador cascada del archivo xml
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Cargando las caracteristicas con numpy
features = np.load('features.npy', allow_pickle=True)

# Cargando las etiquetas con numpy
labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

DIR = r'C:\Users\Home\open_cv\Resources\Faces\val\elton_john\3.jpg'
img = cv.imread(DIR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1,4)

for (x,y,w,h) in faces_rect:
    face_roi = gray[y:y+h, x:x+w]
    
    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {label} or name = {peoples[label]} with a confidence of {confidence}')

    cv.putText(img, f'{peoples[label]}', (20,20), cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0), 1)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=1)
    cv.putText(img, f'Confidence {confidence}', (2,img.shape[0]-20), cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0), 1)

cv.imwrite('./Elton John reconocido.jpg', img)
cv.imshow('Reconocimiento', img)
cv.waitKey(0)