''' Nombre del archivo : neurona.py

Descripcion: Red neuronal multicapa capaz de aprender xor y otras operaciones
booleanas basicas. Requiere de un archivo de configuracion con el numero de
neuronas a usar por capa, la tasa de aprendizaje y la cantidad de iteraciones
a correr.

Uso: python neurona.py config.dat

Notas: Es necesario contar con el modulo numpy.
'''
import numpy
from sys import argv
TASA_APRENDIZAJE = None

debug = False
for i in range(len(argv)):
    if argv[i]=="-b":	  	
        print "*--- Modo Debug ---*" 	
        debug = True

Tabla_Verdad = [([0, 0], 0), 
		([0, 1], 1), 
		([1, 0], 1), 
		([1, 1], 0)]

def configuracion(archivo):
    f = open(archivo, "r")
    config = []
    for line in f.readlines():
	if not "#" in line:
	    _,value = line.split(" ")
	    config.append(value)
    return int(config[0]), int(config[1]), int(config[2]), float(config[3]), int(config[4])

class RedNeuronal(object):
    
    def __init__(self, n_entrada, n_oculta, n_salida):
        self.error = None
        self.entrada = Capa(n_entrada)
	self.oculta = Capa(n_oculta)
	self.salida = Capa(n_salida)
       	self.inicializar_pesos()
	self.salidas = []

    def inicializar_pesos(self):
	self.oculta.w = numpy.random.random((self.oculta.n, self.entrada.n+1)) 
        self.salida.w = numpy.random.random((self.salida.n, self.oculta.n + 1))

     
    def procesar(self, input):
        self.entrada.output[:-1, 0] = input
        self.entrada.output[-1:, 0] = 1.0

	self.oculta.activacion = numpy.dot(self.oculta.w, self.entrada.output)
	self.oculta.output[:-1, :] = numpy.tanh(self.oculta.activacion)
        self.oculta.output[-1:, :] = 1.0
	  
	self.salida.activacion = numpy.dot(self.salida.w, self.oculta.output)
	self.salida.output = numpy.tanh(self.salida.activacion)
	self.salidas.append(self.salida.output[0])
    if debug:
        print self.salida.output[0]
	if self.salida.output[0] > 0.5:
	    return 1
	else:
	    return 0
	
    def entrenar(self, muestra):
        error = self.salida.output - numpy.array(muestra, dtype=float) 
         
        self.salida.delta = (1 - numpy.tanh(self.salida.activacion)) * numpy.tanh(self.salida.activacion) * error
                 
        self.oculta.delta = (1 - numpy.tanh(self.oculta.activacion))\
	 * numpy.tanh(self.oculta.activacion) * numpy.dot(self.salida.w[:,:-1].transpose(), self.salida.delta)
                 

        self.oculta.w = self.oculta.w - TASA_APRENDIZAJE * numpy.dot(self.oculta.delta, self.entrada.output.transpose()) 
        self.salida.w = self.salida.w - TASA_APRENDIZAJE * numpy.dot(self.salida.delta, self.oculta.output.transpose())


class Capa(object):
  def __init__(self, n):
    self.n = n
    self.w = None
    self.activacion = numpy.zeros((self.n, 1), dtype = float)
    self.output = numpy.zeros((self.n+1, 1), dtype = float)
    self.delta = numpy.zeros((self.n), dtype = float)

def main():
    global TASA_APRENDIZAJE
    n_entrada, n_oculta, n_salida, TASA_APRENDIZAJE, iteraciones = configuracion(argv[1])
    red = RedNeuronal(n_entrada, n_oculta, n_salida)
    y = 0
    bien, mal = 0, 0
    for i in range(iteraciones):
        muestra = numpy.random.randint(0, len(Tabla_Verdad))

	t = Tabla_Verdad[muestra][1]
	y = red.procesar(Tabla_Verdad[muestra][0])

	if y != t:
	  mal += 1
          red.entrenar(t)
	else:
	  bien += 1
    if debug:
        print "%s Salida de la Red: %s   Salida Correcta: %s"%(i+1, y, t)
    
    if debug:
        print "Totales"
    
    if debug:
        print "Correctos: %s"%(bien)
    
    if debug:
        print "Incorrectos: %s"%(mal)

main()
