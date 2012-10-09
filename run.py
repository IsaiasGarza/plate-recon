#!/usr/bin/python
import os
zero = '\0'
os.system("python neurona.py > datos.dat")
os.system('grep "00 " datos.dat > 00.dat')
os.system('grep "01 " datos.dat > 01.dat')
os.system('grep "11 " datos.dat > 11.dat')
os.system('sed -i "s/00 //g" 00.dat')
os.system('sed -i "s/01 //g" 01.dat')
os.system('sed -i "s/11 //g" 11.dat')
os.system('gnuplot points.plot')
