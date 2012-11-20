#!/usr/bin/python 
                                                                                                                                            
from random import *
from numpy import *
from numpy.random import *
from sys import argv
import sys

alpha = 0.3
umbral = 0.6
DEBUG = True


class Neurona(object):

	def __init__(self, n):
    		self.w = uniform(low=0, high=1, size=(1, n))
		self.w = append(self.w, umbral)
	def activacion(self, x):
		x = array(x)
		x = append(x, -1)
		act = self.w * x
		
		act = act.sum()
		if act > 0:
			return "1"
		else:
			return "0"
	def aprendizaje(self, y, t, x):
		#print self.w
		for i in range(self.w.size-1):
      			self.w[i] += alpha*(t - y)*x



if __name__ == "__main__":
	ITER = int(argv[1])
	n = int(argv[2])
	capa_oculta = []
	for i in range(n):
		capa_oculta.append(Neurona(1))
        #print argv[3]
	if len(argv) > 3:
	 	fn = argv[3]
		f = open(fn, 'r')
		muestra = []
		for line in f.readlines():
			asd = line.split()
			tmp = []
			for i in range(1, 8):
				if not "\n" in asd[i]:
					tmp.append(float(asd[i]))
			muestra.append([asd[0], tmp])
	for m in muestra:
	  print m
	sys.exit()
	bien = 0
	mal = 0
	for i in range(ITER):
		y = ""
		t = ""
		rnd = randint(0, len(muestra))
		x = muestra[rnd][1]
		t = muestra[rnd][0]
		#print x

		for j in range(len(capa_oculta)):
			y += capa_oculta[j].activacion(x[j])

		if y == t:
			#if DEBUG: print "y = %s t= %s   :)"%(y, t)
			bien += 1
		else:
			#if DEBUG: print "y = %s t= %s   :C"%(y, t)
			mal += 1
			for j in range(len(capa_oculta)):
				if y[j] != t[j]:
					capa_oculta[j].aprendizaje(int(y[j]), int(t[j]), x[j])

	if DEBUG: print "Bien ",bien
	if DEBUG: print "Mal ",mal
        

