''' Nombre del archivo : preprocesamiento.py

Descripcion: Este programa preparara la imagen para poder obtener los datos de entrada.

Uso: python preprocesamiento.py nombreimagen.jpg

Nota: Debe existir una carpeta outputs en la misma donde se encuentre
el archivo para poder almacenar las imagenes filtradas
'''

import cv2
from sys import argv

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
i = 1
input_img = argv[1]
img = cv2.imread(input_img)
DELAY = 1500

cv2.imshow('Original', img)
cv2.waitKey(DELAY)
cv2.destroyWindow('Original')

#grayscale
def convert_grayscale(img):
  global i
  img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  cv2.imwrite('outputs/output%s.jpg'%i, img)
  i+=1
  cv2.imshow('Grayscale', img)
  cv2.waitKey(DELAY)
  cv2.destroyWindow('Grayscale')
  return img

#Blur
def blur_image(img):
  global i
  img = cv2.GaussianBlur(img,(3,3),0)
  cv2.imwrite('outputs/output%s.jpg'%i, img)
  i+=1
  cv2.imshow('Blur', img)
  cv2.waitKey(DELAY)
  cv2.destroyWindow('Blur')
  return img

#Dilatacion
def dilate_image(img):
  global i
  img = cv2.dilate(img, element)
  cv2.imwrite('outputs/output%s.jpg'%i, img)
  i+=1
  cv2.imshow('Dilatacion', img)
  cv2.waitKey(DELAY)
  cv2.destroyWindow('Dilatacion')
  return img


#Threshold
def threshold_image(img, umb, _type):
  global i
  (thresh, img) = cv2.threshold(img, umb, 255, _type)
  cv2.imwrite('outputs/output%s.jpg'%i, img)
  i+=1
  cv2.imshow('Threshold', img)
  cv2.waitKey(DELAY)
  cv2.destroyWindow('Threshold')
  return img

#Erosion
def erode_image(img):
  global i
  img = cv2.erode(img, element)
  cv2.imwrite('outputs/output%s.jpg'%i, img)
  i+=1
  cv2.imshow('Erosion', img)
  cv2.waitKey(DELAY)
  cv2.destroyWindow('Erosion')
  return img

def main():
  global img
  img = blur_image(img)
  img = threshold_image(img, 128, cv2.THRESH_TOZERO)
  #posterizacion
  #img = dilate_image(img)
  img = convert_grayscale(img)
  img = threshold_image(img, 180, cv2.THRESH_OTSU)
 # img = dilate_image(img)


main()


