''' Nombre del archivo : pre_caracter.py

Descripcion: Programa para obtener datos de las letras de la placa.
Encuentra los caracteres en la placa y los segmenta en diferentes
imagenes.

Uso: python pre_caracter.py imagen.png

'''
import cv2
from sys import argv
import numpy
import ImageTk, Image
import Tkinter as tk
import math

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(7,5))
input_img = argv[1]
img = cv2.imread(input_img)

def convert_grayscale(img):
  img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  return img

def smooth_image(img):
  img = cv2.GaussianBlur(img,(5,5),0)
  return img

def threshold_image(img, umb, _type):
  (thresh, img) = cv2.threshold(img, umb, 255, _type)
  return img

def dilate_image(img):
  img = cv2.dilat(img, element)
  return img

def erode_image(img):
  img = cv2.erode(img, element)
  return img


def pintar(old, x1, y1, x2, y2):
  pix = old.load()
  x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
  for i in range(x1, x2):
    for j in range(y1, y2):
       if pix[i, j] == 255:
	 return True
  return False

def verificar_pixeles(old, y):
  w, h = old.size
  pix = old.load()
  x, x1 = 0, w
  for i in range(x, x1):
    #print i, y
    if pix[i, y] == 255:
	return False
  return True
	  


def cortar_imagen():
  old = Image.open('output.png')
  #print old.mode
  ##print old.mode
  w, h = old.size
  root = tk.Tk()
  pix = old.load()
  a, b = int(0.5*h), int(0.5*h)
  x1, x2 = 0, w
  y1, y2 = 0, 0
  done = False
  d_a = False
  d_b = False
  for i in range(w/2):
    for j in range(h/2 - 1):
      if verificar_pixeles(old, a):
	y1 = a
	d_a = True
      else:
	a += 1
	if a >= h: a, d_a = h-1, True
      if verificar_pixeles(old, b):
	y2 = b
	d_b = True
      else:
        b -= 1
	if b < 0: b, d_b = 0, True
      if d_a and d_b:
	done = True
	break
    if done:
	break
     
  box = (x1, y2, x2, y1)      
  #print box
  old = old.crop(box)
  w, h = old.size
  #old = old.resize((w, 70), Image.NEAREST)
  old.save('output.png', 'PNG')
  return box

def close(x, w, x1, x2):
  if x1 in range (x-5, x+5):
    #print 'yes'
    return True
  elif x2 in range (w-5, w+5):
    #print 'yes1'
    return True
  else:
    return False

def main():
  global img
  asd = img
  img = convert_grayscale(img)
  img = smooth_image(img)
  img = threshold_image(img, 128, cv2.THRESH_BINARY_INV)
  img = erode_image(img)
  cv2.imwrite('output.png', img)
  cortar_imagen()
  img = cv2.imread('output.png')
  gray = convert_grayscale(img)
  contours, hierarchy = cv2.findContours(gray, mode=cv2.RETR_LIST,method=cv2.CHAIN_APPROX_SIMPLE )
  done = True
  rects = []
  for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    w = w + x
    h = h + y
    #print h-y
    if (h-y) > 60:
      ##print x, y, w, h
      rects.append([x, y, w, h])
  i = 0
  rects.sort()
  for rect in rects:
    x, y, w, h = rect[0], rect[1], rect[2], rect[3]
    #cv2.rectangle(img,(x,y),(w,h),(255, 0, 0),2)
    cv2.imwrite('output_%s.png'%i, img[y:h, x:w])
    i+=1
  cv2.imwrite('output.png', img)
  for k in range(len(rects)):
    im = Image.open('output_%s.png'%k)
    im2 = im.resize((30, 70), Image.NEAREST)
    ##print im2.size
    im2.save('output_%s.png'%k, 'PNG')

main()

