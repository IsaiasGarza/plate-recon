#Perceptron

from random import randint, random

LENGTH = 2+1
THRESHOLD = 1.5
LEARNING_RATE = 0.75
FILE = 'muestras.dat'

def buildWeights():
    weights = [0] * LENGTH
    for i in range(LENGTH-1):
        weights[i] = float('%.2f' % random())
    weights[LENGTH-1] = THRESHOLD
    return weights

def buildInputs():
    inputs = [0] * LENGTH
    for i in range(LENGTH-1):
        inputs[i] = randint(0,1)
    inputs[LENGTH-1] = -1
    return inputs

def readFile():
    f = open(FILE, 'r')
    lines = f.readlines()
    f.close()
    return lines

def TLU(inputs,weights):
    activation = 0
    for i in range(LENGTH):
        activation += ( float(inputs[i]) * weights[i] )
    if activation < 0:
        return 0
    else:
        return 1

def updateWeights(weights, inputs, t, y):
    newWeights = [0] * LENGTH
    for i in range(LENGTH):
        newWeights[i] = LEARNING_RATE * (int(t)-y) * float(inputs[i])
    return newWeights

def main():
#    weights = buildWeights()
    weights =  [-0.046696788143325, -0.30724436939175, 0.75]
    bien = mal = 0
    lines = readFile()
    for l in lines:
        v = l.split(' ')
        y = TLU([v[0],v[1],-1], weights)
        if y is not int(v[2]):
            mal += 1
#            print '\nViejo: ' + str(weights)
            weights = updateWeights(weights,[v[0],v[1],-1], v[2], y)
#            print 'Nuevo: ' + str(weights) + '\n'
        else:
            bien += 1
    print 'Mal:' + str(mal)
    print 'Bien: ' + str(bien)
    print 'Weights: ' + str(weights)

if(__name__ ==  '__main__'):
    main()
