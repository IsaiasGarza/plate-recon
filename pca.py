''' Nombre del archivo : pca.py

Descripcion: Aplica el PCA a una imagen binarizada para obtener
las caracteristicas de la misma

Uso: python pca.py imagen.png

Notas: Es necesario contar con los modulos mdp, numpy y PIL.
'''


import mdp
import numpy as np
import random
import Image

im = Image.open("output.png")
pix = im.load()
w, h = im.size
x = []

for i in range(h):
  tmp = []
  for j in range(w):
    if pix[j, i] == 255:
      tmp.append(1)
    else:
      tmp.append(0)
  x.append(tmp)

# perform PCA on some data x
y = mdp.pca(np.array(x,dtype = np.float64 ), output_dim = 1)
for vect in x:
  print vect
suma = 0
for value in y:
  suma += value
print value
