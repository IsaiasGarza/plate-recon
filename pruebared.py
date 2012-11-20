from numpy import *
from random import *
from sys import argv

debug = False
for i in range(len(argv)):
    if argv[i]=="-b":	  	
        print "*--- Modo Debug ---*" 	
        debug = True

class pruebared(object):
	def __init__(self):
		(self.vectorEntr, self.largo, self.dimension) = self.entradas()
		self.vectorPeso = self.pesos(self.largo, self.dimension)
		self.vectorSalida = self.pesos(self.largo, self.dimension - 2)

	def entradas(self):
		f = open('muestra.roi','r')

		lista1 = []
		lista2 = []

		for i in f.readlines(): #Leemos todo el archivo 	
			i = i.split() #Separarlo uno por uno
			lista1.append(i) # Agregamos las coordenas a la lista.

		dimension = len(lista1[0]) + 1 # Para hacer a las dimenciones variables


		for i in lista1:
			for j in i:
				lista2.append(j)
			lista2.append(-1)

		largo = len(lista2) / dimension

		for i in range(largo):
			var1 = int(lista2.pop(0))
			var2 = int(lista2.pop(0))
			var3 = int(lista2.pop(0))
			var4 = int(lista2.pop(0))
			var5 = int(lista2.pop(0))
			lista2.append((var1, var2, var3, var4, var5))

		vectorEntr = empty((largo, dimension)) # Creamos una matriz | PARAMETROS => ((filas(-), columnas(|)))

		for i, valor1 in enumerate(lista2):
			for j, valor2 in enumerate(valor1):
				vectorEntr[i][j] = valor2

		if debug: print "\nVector de Entrada ----> \n" + str(vectorEntr)
		return (vectorEntr, largo, dimension)

	def pesos(self, largo, dimension):
		vectorPeso = empty((largo, dimension)) 
		for i in range(largo):
			for j in range(dimension):
				vectorPeso[i][j] = uniform(-1, 1)

		if debug: print "\nVector de Pesos ----> \n"+ str(vectorPeso)
		return vectorPeso

	def activacion(self, largo, vectorEntr, vectorPeso):
		valor = sum(vectorEntr * vectorPeso)
		return valor

def main():
	neuro = pruebared()

	(vectorEntr, largo, dimension) = (neuro.vectorEntr, neuro.largo, neuro.dimension)

	for i in vectorEntr:
		if debug: print "Capa = ", i
		neuro.i = i
		neuro.capa = neuro.activacion(neuro.largo, neuro.i, neuro.vectorPeso)
		neuro.capaSali = neuro.activacion(neuro.largo, neuro.capa, neuro.vectorSalida)

	print "\nValor de la capa ---> \n"+str(neuro.capa)
	print "\nValor de la salida ---> \n"+str(neuro.capaSali)
	#vectorPeso = neuro.activacion(largo, dimension, vectorEntr, nuevo.vectorPeso)
	#vectorSalida = neuro.activacion(largo, dimension - 1, vectorEntr, nuevo.vectorPeso)

main()
