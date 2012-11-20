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
from sys import argv

debug = False
for i in range(len(argv)):
    if argv[i]=="-b":	  	
        print "*--- Modo Debug ---*" 	
        debug = True

f = open('muestras.dat', 'w')
abec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


correcto = ['P', 'W', '3', '7', '6', '8', '8', 'D', 'Z', 'G', '2', '0', '1', 'R', 'S', '2', '0', '0']
for k in range(len(correcto)):
	im = Image.open("muestras/%s.png"%k)
	pix = im.load()
	w, h = im.size
	x = []

	for i in range(w):
	  tmp = []
	  for j in range(h):
	    if pix[i, j] == (255, 255, 255):
	      tmp.append(1)
	    else:
	      tmp.append(0)
	  x.append(tmp)
	
	y = mdp.pca(np.array(x,dtype = np.float64 ), output_dim = (7))
	y = y.transpose()
	res = []
	for value in y:
		res.append(value.sum()*1.0e+14)
	y = res
	f.write("%s "%bin(abec.index(correcto[k]))[2:].zfill(7))
	for value in y:
	  f.write("%s "%(str(value))) 
	f.write("\n")
	if debug: print "Dato para la imagen %s: %s\n"%(k, y)
