''' Nombre del archivo : pre_caracter.py

Descripcion: Programa para obtener datos de las letras de la placa.

Uso: python pre_caracter.py imagen.png

'''

import cv2
from sys import argv
import numpy
import ImageTk, Image
import Tkinter as tk

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(6,6))
input_img = argv[1]
img = cv2.imread(input_img)

def convert_grayscale(img):
  img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  return img

def threshold_image(img, umb, _type):
  (thresh, img) = cv2.threshold(img, umb, 255, _type)
  return img

def dilate_image(img):
  img = cv2.dilate(img, element)
  return img

def erode_image(img):
  img = cv2.erode(img, element)
  return img


def pintar(old, x1, y1, x2, y2):
  pix = old.load()
  x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
  for i in range(x1, x2):
    for j in range(y1, y2):
       if pix[i, j] == 0:
	 return True
  return False



def escala():
  img = Image.new('L', (10,14))
  old = Image.open('roi.png')
  print old.mode
  w, h = old.size
  root = tk.Tk()
  canvas = tk.Canvas(root, width = w, height = h)
  canvas.pack(side = 'top', fill = 'both', expand = 'yes')
  photo = ImageTk.PhotoImage(old)
  canvas.create_image(0, 0, image = photo, anchor = 'nw')
  vel_w = (w)/10
  vel_h = (h)/14
  pix = img.load()
  for i in range(w/vel_w):
    for j in range(h/vel_h):
      x1, y1, x2, y2 = 0+(i*vel_w), 0+(j*vel_h), vel_w+(i*vel_w), vel_h+(j*vel_h)
      if pintar(old, x1, y1, x2, y2 ) == True:
        if i < 10 and j < 14:
          #print i, j 
	  pix[i, j] = 0
        rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill = "black", width = 1)
      else:
        if i < 10 and j < 14:
          #print i, j 
	  pix[i, j] = 255
        rectangle = canvas.create_rectangle(x1, y1, x2, y2, outline = "red", width = 1)
  img.save("output.png", "PNG")
  root.mainloop()

def main():
  global img
  img = convert_grayscale(img)
  img = dilate_image(img)
  img = threshold_image(img, 128, cv2.THRESH_OTSU)
  contours, hierarchy = cv2.findContours(img.astype('uint8'), mode=cv2.RETR_LIST,method=cv2.CHAIN_APPROX_SIMPLE )
  x,y,w,h = cv2.boundingRect(contours[10])
  print contours
  cv2.imwrite('roi.png', img[y:y+h, x:x+w])
  #escala()

main()

