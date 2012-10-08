''' Nombre del archivo : entrenamiento1.py

Descripcion: Programa que carga las imagenes de muestra
individualmente para poder seleccionar las coordenadas donde se
encuentra nuestra region de interes.

Uso: python entrenamiento1.py

Nota: Debe existir una carpeta imagenes donde se encuentren las
diferentes imagenes de muestra que se utilizaran, numeradas del 1
en adelante. 
'''



import Tkinter as tk
import ImageTk, Image

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open("imagenes/1.jpg"))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
i = 1
count = 0
x1, y1, x2, y2 = 0, 0, 0, 0

f = open("muestra.roi", "w")

def callback(e):
  img2 = ImageTk.PhotoImage(Image.open(path2))
  panel.configure(image = img2)
  panel.image = img

def click(event):
  global count, x1, x2, y1, y2, i, panel
  count+=1
  if count == 1:
    x1, y1 = event.x, event.y
  elif count == 2:
    x2, y2 = event.x, event.y
    count = 0
    f.write("%s %s %s %s %s\n"%(i, x1, y1, x2, y2))
    i+=1
    new = ImageTk.PhotoImage(Image.open("imagenes/%s.jpg"%i))
    panel.configure(image = new)
    panel.image = new
  print event.x, event.y

def key(event):
  global i, panel, count, x1, x2, y1, y2, f
  if count >= 2:
    f.write("%s %s %s %s %s\n"%(i, x1, y1, x2, y2))
    i+=1
    new = ImageTk.PhotoImage(Image.open("imagenes/%s.jpg"%i))
    panel.configure(image = new)
    panel.image = new
    count = 0
  else:
    print "Define los dos pares de coordenadas antes de continuar"

root.bind("<Return>", callback)
root.bind("<Double-1>", click)
root.bind("<Key>", key)
root.mainloop()
