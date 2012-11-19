#!/usr/bin/python 
                                                                                                                                            
from random import *
from numpy import *
from numpy.random import *
from sys import argv



alpha = 0.1

umbral = 0.5


class Capa(object):
	def __init__(self, n, name):
		self.name = name
		self.neuronas = self.agregar_neurona(n)
	
	def agregar_neurona(self, n):
		for i in range(n):
			self.neuronas.append(Neurona(1))
	def procesar(self, x):
		x = append(x, -1)
		w = array()
		for neurona in neuronas:
			w = append(neurona.w)
		w = append(umbral)
		act = w*x
		act = act.sum()
		if act > 0:
			return 1
		else:
			return 0
		

class Neurona(object):

	def __init__(self, n):
    		self.w = uniform(low=0, high=1, size=(1, n))
		self.w = append(self.w, umbral)
	def activacion(self, x):
		a = x
		x = append(x, -1)
		act = self.w * x
		act = act.sum()
		if act > 0:
			return "1"
		else:
			return "0"
	def aprendizaje(self, y, t, x):
		for i in range(self.w.size-1):
      			self.w[i] += alpha*(t - y)*x



if __name__ == "__main__":
	ITER = int(argv[1])
	n = int(argv[2])

	capa_oculta = []
	for i in range(n):
		capa_oculta.append(Neurona(1))
	bien = 0
	mal = 0

	for i in range(ITER):
		y = ""
		t = ""
		muestra = []
		for j in range(len(capa_oculta)):
		 	muestra.append(uniform(0, 1))
	
		for x in muestra:
			if x > 0.5:
				t += "1"
			else:
				t += "0"

		for j in range(len(capa_oculta)):
			y += capa_oculta[j].activacion(muestra[j])
	
		print "Salida de la Neurona: %s Salida Correcta: %s"%(y, t)

		if y == t:
			bien += 1
		else:
			mal += 1
			for j in range(len(capa_oculta)):
				if y[j] != t[j]:
					capa_oculta[j].aprendizaje(int(y[j]), int(t[j]), muestra[j])

	print "Bien ",bien
	print "Mal ",mal

