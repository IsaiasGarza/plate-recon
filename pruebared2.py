from numpy import *
from random import *
from sys import argv

debug = False
for i in range(len(argv)):
    if argv[i]=="-b":	  	
        print "*--- Modo Debug ---*" 	
        debug = True

class pruebared2(object):
	def __init__(self):
		(self.vectorEntr, self.dimension) = self.entradas() #Las variables vectorEntr y dimension se obtienen del metodo entradas
		self.vectorPeso = self.pesos(self.dimension, self.dimension) #Las variable vectorPeso se obtienen del metodo pesos
		self.vectorSalida = self.pesos(self.dimension, self.dimension - 2) #Las variable vectorSalida se obtienen del metodo pesos diciendo que la salida debe ser de tamano - 2

	def entradas(self): #Funcion que se encarga de generar las entradas
		f = open('datos.puddi','r')

		lista1 = [] #Arreglo que recibira los datos del archivo
		lista2 = [] #Arreglo de salida

		for i in f.readlines(): #Leemos todo el archivo 	
			i = i.split() #Separarlo uno por uno
			lista1.append(i) # Agregamos los datos a la lista.

		dimension = len(lista1[0]) + 1 #Tamano del vector mas 1 ya que a las entradas se le agrega un -1 y podra ser utilizada esta variable para crear los vectores de Peso.

		for i in lista1: #Haciendo un barrido de la lista en x y en y
			for j in i:
				lista2.append(j) #Agregando los datos del primer arreglo en el segundo
			lista2.append(-1) #Se agrega un -1 a las entradas

		largo = len(lista2) / dimension

		for i in range(largo): #Agregamos cada elemento como uno solo
		#Como la forma de agregar es todo junto pues hay que separarlos uno por uno y agregarlo
			var1 = int(lista2.pop(0))
			var2 = int(lista2.pop(0))
			var3 = int(lista2.pop(0))
			var4 = int(lista2.pop(0))
			var5 = int(lista2.pop(0))
			lista2.append((var1, var2, var3, var4, var5))

		#Esta lista sera el vector de entradas
		vectorEntr = empty((largo, dimension)) # Creamos una matriz vacio (filas(-), columnas(|))
 
		for i, valor1 in enumerate(lista2): #Se utiliza la funcion enumarate para enumerar la lista y los datos se guardan en i, valor1
			for j, valor2 in enumerate(valor1): #Se utiliza la funcion enumarate para enumerar la lista y los datos se guardan en j, valor2
				vectorEntr[i][j] = valor2 #Se guarda en el vector[i][j] lo que vale valor2
		#http://stackoverflow.com/questions/10777271/python-using-enumerate-inside-list-comprehension

		#if debug: print "\nVector de Entrada ----> \n" + str(vectorEntr)
		return (vectorEntr, dimension) #Se regrese el vector de entrada y dimension

	def pesos(self, largo, dimension): #Funcion que crea el vector de Pesos
		vectorPeso = empty((largo, dimension)) #Creamos un arreglo vacio de nxn
		for i in range(largo):
			for j in range(dimension):
				vectorPeso[i][j] = uniform(-1, 1) #Creamos un valor uniforme y los agregamos al vector de peso

		#if debug: print "\nVector de Pesos ----> \n"+ str(vectorPeso)
		return vectorPeso #Regresa el vector de pesos

	def activacion(self, largo, dimension, vectorEntr, vectorPeso):
		#if debug: print "\n"+str(vectorEntr)
		if debug: print "\n"+str(vectorPeso)
		valor = zeros(largo) #Creamos un vector de ceros del tamano n
		for i in range(largo):
			valor[i] = sum(vectorEntr[i] * vectorPeso[i]) #Se agrega la suma de la multiplicacion del vector de entradas y el de pesos al vector[i]
			if debug: print 'valor '+str(i)+' --> '+str(valor[i]) #Para saber lo que vale la variable valor[i]
		return valor

def main():
	neuro = pruebared2() #Creamos un objeto de la clase pruebared2

	#(vectorEntr, largo, dimension) = (neuro.vectorEntr, neuro.largo, neuro.dimension)
	(vectorEntr, dimension) = (neuro.vectorEntr, neuro.dimension) #Se recibe en las variables vectorEntr y dimension lo que vale las variables vectorEntr y dimension de la clase
	#if debug: print "vectorEntradas -->\n"+str(vectorEntr)

	conta = 0
	for i in vectorEntr:
		conta = conta + 1
		if debug: print "\nCapa "+str(conta)+" = "+str(i)
		neuro.i = i
		neuro.capa = neuro.activacion(neuro.dimension, neuro.dimension, neuro.i, neuro.vectorPeso) #Se crea la capa salida del metodo activacion de la clase pruebared2
		neuro.capaSali = neuro.activacion(neuro.dimension, neuro.dimension-2, neuro.capa, neuro.vectorSalida) #Se crea la capa salida del metodo activacion de la clase pruebared2,  se pone un -2 ya que quiero de salida lo que vale la dimension -2

	print "\nValor de la capa ---> \n"+str(neuro.capa)+'\n' #Imprimimos lo que vale la ultima capa
	print "\nValor de la salida ---> \n"+str(neuro.capaSali) #Imprimimos lo que vale la capa de salida
	
	vecs = list()
	for i in neuro.capaSali:
		if i > 0:
			vecs.append(1)
		else:
			vecs.append(0)

	print 'Salida = '+str(vecs)
	#vectorPeso = neuro.activacion(largo, dimension, vectorEntr, nuevo.vectorPeso)
	#vectorSalida = neuro.activacion(largo, dimension - 1, vectorEntr, nuevo.vectorPeso)

main()
