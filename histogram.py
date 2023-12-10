import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('./Resources/Photos/cats.jpg')
#img = cv.imread('./Resources/Photos/cats 2.jpg')

dim = img.shape[:2]
print(dim)
blank = np.zeros(dim, dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
print(gray.shape)

circle = cv.circle(blank.copy(), (dim[1]//2, dim[0]//2), 100,255, -1)
cv.imshow('Mask', circle)

img_masked_gray = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Imagen con Mascara', img_masked_gray)

img_masked_color = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Imagen con Mascara', img_masked_color)

print("*"*100)
cv.imshow('Gato', img)


cv.imshow('Gato Gris', gray)

# GrayScale histogram
# Se puede agregar el parametro mask para calcular la intensidad 
# De los pixeles en esa parte de la imagen

#gray_hist = cv.calcHist([gray],[0], None,[256],[0,256])
gray_hist = cv.calcHist([gray],[0], img_masked_gray,[256],[0,256])
print(gray_hist.shape)

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Colour Histogram

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')

# Para calcular el histograma con mascara de 3 canales
# Se tiene que poner la mascara original, es decir, 
# En escala de grises solo hay 1 canal y se pone el 
# parametro mask con la imagen enmascarada, sin embargo
# en los 3 canales se debe poner lo que se va a poner de
# mascara, en este caso el circulo, para computar cada canal
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color= color)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)