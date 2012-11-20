''' Nombre del archivo : entrenamiento2.py

Descripcion: Programa para obtener los datos de entrenamiento de la segunda
parte, que es un vector de propiedades.

Uso: python entrenamiento2.py num_imagen

Nota: Debe existir un archivo muestra.roi con las coordenadas de la ubicacion
de la placa en cada imagen. Tambien es necesaria una carpeta imagenes donde
se encuentren dichas imagenes numeradas
'''

import Tkinter as tk
import ImageTk, Image
import math
from sys import argv
 
debug = False
for i in range(len(argv)):
    if argv[i]=="-b":
        print "*--- Modo Debug ---*"
        debug = True
min_disc = 10
max_disc = 60



def distancia(x1, y1, x2, y2):
  return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


def calcular_area(x1, y1, x2, y2):
  area = 0
  base = distancia(x1, y1, x2, y1)
  altura = distancia(x1, y1, x1, y2)
  if debug:  
      print base*altura
  return base*altura

def overlap_area(roi, x11, y11, x12, y12):
  
  x21, y21, x22, y22 = roi.x1, roi.y1, roi.x2, roi.y2
  w1 = distancia(x11, y11, x12, y11)
  h1 = distancia(x11, y11, x12, y12)

  w2 = distancia(x21, y21, x22, y21)
  h2 = distancia(x21, y21, x21, y22)

  x = max(0, min(x12,x22) - max(x11, x21))
  y = max(0, min(y12,y22) - max(y11,y21))
  return x*y

class ROI(object):
  def __init__(self, i):
    self.ID = i
    self.x1, self.y1, self.x2, self.y2 = self.get_coords(i)
    self.area = calcular_area(self.x1, self.y1, self.x2, self.y2)
    if debug:  
        print self.x1, self.y1, self.x2, self.y2

  def get_coords(self, n):
    f = open("muestra.roi", "r")
    for line in f.readlines():
      tmp, x1, y1, x2, y2 = line.split(" ")
      if debug:  
         print tmp, n
      if n in tmp:
         return int(x1), int(y1), int(x2), int(y2)
    return -1, -1, -1, -1

n = argv[1]
root = tk.Tk()
img = Image.open("imagenes/%s.jpg"%n)
width, height = img.size[0], img.size[1]
photo = ImageTk.PhotoImage(img)
ancho = 20
largo = 20
vel = 20

canvas = tk.Canvas(root, width = img.size[0], height = img.size[1])
canvas.pack(side = 'top', fill = 'both', expand = 'yes')
canvas.create_image(0, 0, image = photo, anchor = 'nw')
matriz = []

roi = ROI(n)
rectangle = canvas.create_rectangle(roi.x1, roi.y1, roi.x2, roi.y2, outline = "yellow", width = 3)
f = open("muestra.rbi", "w")


for i in range(width/vel):
  tmp = []
  for j in range(height/vel):
    x1, y1, x2, y2 = 0+(i*vel), 0+(j*vel), ancho+(i*vel), largo+(j*vel)
    ov_area = overlap_area(roi, x1, y1, x2, y2)
    rect_area = calcular_area(x1, y1, x2, y2)
    #print area
    if ov_area > 0:
      disc = (ov_area/rect_area)*100
      if debug:  
        print disc
      if disc < min_disc:
        rectangle = canvas.create_rectangle(x1, y1, x2, y2, outline = "red", width = 2)
        tmp.append(-1)
      elif disc > min_disc:
        rectangle = canvas.create_rectangle(x1, y1, x2, y2, outline = "green", width = 2)
	tmp.append(1)
    else:
      rectangle = canvas.create_rectangle(x1, y1, x2, y2, outline = "black")
      tmp.append(0)
  f.write("%s\n"%tmp)
  matriz.append(tmp)





root.mainloop()

