import math

def seleccion(x,y,a,t,s):
	k = 0
	if s == 0:
		k = linear(x,y,t,c)
	if s == 1:
		k = polinomial(a,x,y,t,c)
	if s == 2:
		k = hyp_tan(a, x,y,t,c)
	if s == 3:
		k = rat_quad(x,y,c)
	if s == 4:
		k = multiquad(x,y,c)
	if s == 5:
		k = inv_multiquad(x,y,c)
	if s == 6:
		k = power_kernel(x,y,c)
	if s == 7:
		k = log_kernel(x,y,c)
	if s == 8:
		k = t_student(x,y,c)
	return k

def linear(x,y,T,c):
     k = ((x**T)*y)+c
     return k
 
def polinomial(a,x,y,T,c):
     k = ((a*x**T)*y)+c
     return k
 
def hyp_tan(a,x,y,T,c):
     k = math.tanh(((a*x**T)*y)+c)
     return k

def rat_quad(x,y,c):
     k = 1 - (math.fabs(x-y)**2/(math.fabs(x-y)**2)+c)
     return k
 
def multiquad(x,y,c):
     k = math.sqrt((math.fabs(x+y)**2)+c**2)
     return k
 
def inv_multiquad(x,y,c):
     k = 1/(math.sqrt((math.fabs(x+y)**2)+c**2))
     return k
 
def power_kernel(x,y,d):
     k = -((math.fabs(x+y)**d)+1)
     return k

def log_kernel(x,y,d):
     k = -(math.log(math.fabs(x-y)**d) +1 )
     return k

def t_student(x,y,d):
     k = 1/(1+(math.fabs(x+y)**2))
     return k