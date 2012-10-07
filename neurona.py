#!/usr/bin/python
import random
from sys import argv
from numpy import *
from numpy.random import *
import random
import sys

alpha = .3
DIM = 1
N_MUESTRAS = 500

def generar_muestras(a, b, n):
  f = open("muestra.txt","w") 
  for i in range(n):
    muestra = random.uniform(0, (a+b))
    if muestra < b:
      f.write("%s %s\n"%(muestra, "00"))
    elif (muestra > b) and (muestra < a):
      f.write("%s %s\n"%(muestra, "01"))
    elif muestra >a:
      f.write("%s %s\n"%(muestra, "11"))
  f.close()

def leer_muestra(filename):
  f = open(filename, "r")
  m = []	
  c = []
  for line in f.readlines():
      tmp_m, tmp_c = line.split(" ") 
      m.append(float(tmp_m))
      c.append(tmp_c.replace("\n", ""))
  f.close()
  return array(m), array(c)

def generar_pesos(n):
  w = uniform(low=-1, high=1, size=(1,n+1))
  return w


class Neurona:
  def __init__(self, n, ID):
    self.x = None
    self.w = generar_pesos(n)
    self.n = n
    self.res = None
    self.ID = ID

  def procesar(self, x):
    self.x = array([])
    self.x = append(self.x, x)    
    self.x = append(self.x, -1)
    a = self.w * self.x
    self.res = a.sum()
    if self.res > 0:
      return "1"
    else:
      return "0"
 
  def entrenar(self, y, t, muestra):
    global alpha
    for i in range(len(self.w)):
      self.w[i] += alpha*(t - y)*muestra
   
def main():
  global DIM, N_MUESTRAS
  generar_muestras(5, 2, N_MUESTRAS)
  m, c = leer_muestra("muestra.txt")
  a = Neurona(DIM, "a")
  b = Neurona(DIM, "b")
  neuronas = []
  neuronas.append(a)
  neuronas.append(b)
  bien = 0
  mal = 0
  for i in range(len(m)):
    generado = ""
    deseado = c[i]
    muestra = m[i]
    for neurona in neuronas:
      generado += neurona.procesar(muestra)
    print "%s %s, %s"%(deseado, neuronas[0].res, neuronas[1].res)
    #print "%s == %s"%(deseado, generado)
    if generado == deseado:
      bien += 1
    else:
      mal += 1
      for j in range(len(generado)):
 	if generado[j] != deseado[j]:
          y = bool(int(generado[j]))
          t = bool(int(deseado[j]))
	  neuronas[j].entrenar(y, t, muestra)
  print "Bien: %s"%bien
  print "Mal: %s"%mal
      
    
main()
