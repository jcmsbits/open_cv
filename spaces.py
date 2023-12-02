import cv2 as cv
import matplotlib.pyplot as plt

#La libreria de Matplotlib usa RGB y OpenCV BGR

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Parque', img)

# No funciona pero la idea es que no se ve como la imagen original
# plt.imshow(img)
# plt.show()

# BGR(que viene por defecto cv) -> Grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Parque Gris', gray_img)

# BGR -> HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('Parque Gris', hsv_img)

# BGR -> L*A*B (El formato esta adaptado a como los humanos percibimos el color)
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('L.A.B', lab)


# BGR -> RGB
rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB Image',rgb_img)
plt.imshow(rgb_img)
plt.show()


# Para llevar de HSV a LAB tiene que convertirse primero a BGR y viceversa
# Asi sucede para los demas

# RGB -> BGR
bgr_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2BGR)
cv.imshow('Convertido a RGB',bgr_img)

# HSV -> BGR
bgr_img = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)
cv.imshow('Convertido de HSV', bgr_img)


cv.waitKey(0)
