import os
import cv2 as cv
import numpy as np


haar_face = cv.CascadeClassifier('haar_face.xml')
peoples = ['Ben Afflek', 'Elton John','Jerry Seinfield','Madonna','Mindy Kaling']

p = []

DIR = r'C:\Users\Home\open_cv\Resources\Faces\train'

# Tomar el directorio como una lista de nombre de carpetas con os.listdir
# for i in os.listdir(DIR):
#     print(i)
#     p.append(i)

# print(p)

# features va a las caras recortadas de las imagenes
features = []
labels = []

def create_train():
    
    for person in peoples:
        # Entrando a una subcarpeta con os.path.join
        path = os.path.join(DIR, person)
        # Obteniendo el índice de cada persona
        label = peoples.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array =  cv.imread(img_path)
            img_gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_face.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = img_gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)



create_train()

# 100 imagenes con etiquetas
# print(f'length of the features = {len(features)}')
# print(f'length of the features = {len(labels)}')

# Entrenando nuestro reconocedor de caras

face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Primero pasamos features y labels que son listas a array de numpy
print('Training done--------------------------------')

features = np.array(features, dtype='object')
labels = np.array(labels)

# Train the Recognizer on the features list and the labels list

face_recognizer.train(features, labels)
# Se puede guardar el modelo con un archivo yaml
face_recognizer.save('face_trained.yml')

# Para salvar los array se usa el metodo np.save de numpy
np.save('features.npy',features)
np.save('labels.npy', labels)