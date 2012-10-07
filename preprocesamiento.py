''' Nombre del archivo : preprocesamiento.py

Descripcion: Este programa preparara la imagen para poder obtener los datos de entrada.

Uso: python preprocesamiento.py nombreimagen.jpg'''


import cv2
from sys import argv

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2))
i = 1
input_img = argv[1]
img = cv2.imread(input_img)
DELAY = 1500

cv2.imshow('Original', img)
cv2.waitKey(DELAY)
cv2.destroyWindow('Original')

#Gray
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('../outputs/output%s.jpg'%i, img)
i+=1
cv2.imshow('Grayscale', img)
cv2.waitKey(DELAY)
cv2.destroyWindow('Grayscale')
"""
#Blur
img = cv2.GaussianBlur(img,(5,5),0)
cv2.imwrite('../outputs/output%s.jpg'%i, img)
i+=1
cv2.imshow('Blur', img)
cv2.waitKey(DELAY)
cv2.destroyWindow('Blur')"""

#Threshold
(thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)
cv2.imwrite('../outputs/output%s.jpg'%i, img)
i+=1
cv2.imshow('Threshold', img)
cv2.waitKey(DELAY)
cv2.destroyWindow('Threshold')

#Dilate
img = cv2.dilate(img, element)
cv2.imwrite('../outputs/output%s.jpg'%i, img)
i+=1
cv2.imshow('Dilatacion', img)
cv2.waitKey(DELAY)
cv2.destroyWindow('Dilatacion')

"""
#Erode
img = cv2.erode(img, element)
cv2.imwrite('../outputs/output%s.jpg'%i, img)
i+=1
cv2.imshow('Erosion', img)
cv2.waitKey(DELAY)
cv2.destroyWindow('Erosion')
"""

