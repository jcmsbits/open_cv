import cv2 as cv

#img = cv.imread('Resources/Photos/cat.jpg')
"""
    La imagen se puede desbordar de la pantalla
"""
#img = cv.imread('Resources/Photos/cat_large.jpg')

#Da un error (-215) que no puede encontrar la imagen
#img = cv.imread('Resources/Photos/cat_large2.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

#Leyendo Videos

#La Mayoria de las veces el argumento 0 en VideCapture es la webcam
#o 1 para para otra camara agregada y asi sucesivamente
# capture = cv.VideoCapture('Resources/Videos/dog.mp4')
# Da error de -215 al finalizar el video porque no encuentra mas fotogramas
# while True:
#     isTrue, Frame = capture.read()
#     cv.imshow('Video', Frame)

#     if cv.waitKey(20) & 0xff ==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()