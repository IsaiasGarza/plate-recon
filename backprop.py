import math,random

class red:
  def __init__(self, inputs, hiddens, outputs):
    self.inputNode = inputs + 1
    self.hiddenNode = hiddens
    self.outputNode = outputs
    self.activationI, self.activationH, self.o = [],[], []
    self.activationI = [1.0]*self.inputNode
    self.activationH = [1.0]*self.hiddenNode
    self.activationO = [1.0]*self.outputNode
    self.weightI = matr(self.inputNode, self.hiddenNode)
    self.weightO = matr(self.hiddenNode, self.outputNode)
    randMatr( self.weightI, -0.2, 0.2 )
    randMatr( self.weightO, -2.0, 2.0 )
    self.changeI = matr(self.inputNode, self.hiddenNode)
    self.changeO = matr(self.hiddenNode, self.outputNode)

  def execute(self, inputs):
    if len(inputs) != self.inputNode-1:
      print 'number of inputs wrong'    
    for i in range(self.inputNode-1):
      self.activationI[i] = inputs[i]
    for j in range(self.hiddenNode):
      sum = 0.0
      for i in range(self.inputNode):
        sum +=( self.activationI[i] * self.weightI[i][j] )
      self.activationH[j] = sigmoid(sum)
    for k in range(self.outputNode):
      sum = 0.0
      for j in range(self.hiddenNode):        
        sum +=( self.activationH[j] * self.weightO[j][k] )
      self.activationO[k] = sigmoid(sum)
      
    return self.activationO

  def backPropagate(self, targets, N, M):
    output_deltas = [0.0] * self.outputNode
    for k in range(self.outputNode):
      error = targets[k] - self.activationO[k]
      output_deltas[k] =  error * dsigmoid(self.activationO[k]) 
    for j in range(self.hiddenNode):
      for k in range(self.outputNode):
        change = output_deltas[k] * self.activationH[j]
        self.weightO[j][k] += N*change + M*self.changeO[j][k]
        self.changeO[j][k] = change
    hidden_deltas = [0.0] * self.hiddenNode
    for j in range(self.hiddenNode):
      error = 0.0
      for k in range(self.outputNode):
        error += output_deltas[k] * self.weightO[j][k]
      hidden_deltas[j] = error * dsigmoid(self.activationH[j])
    for i in range(self.inputNode):
      for j in range(self.hiddenNode):
        change = hidden_deltas[j] * self.activationI[i]
        self.weightI[i][j] += N*change + M*self.changeI[i][j]
        self.changeI[i][j] = change
    error = 0.0
    for k in range(len(targets)):
      error = 0.5 *(targets[k]-self.activationO[k])**2
    return error
        
        
  def weights(self):
    for i in range(self.inputNode):
      print self.wi[i]
    print
    print 'Output weights:'
    for j in range(self.hiddenNode):
      print self.weightO[j]
    print ''
  
  def test(self, a):
    for i in a:
      inputs = i[0]
      print i[0], ':', self.execute(inputs), '\tTarget', i[1]

  def entrena(self, patr, itera = 1000, N=0.5, M=0.1):
    for i in range(itera):
      for p in patr:
        inputs = p[0]
        targets = p[1]
        self.execute(inputs)
        error = self.backPropagate(targets, N, M)
      if i % 50 == 0:
        print 'Error', error
    self.test(patr)

def sigmoid(x):
  return math.tanh(x)

def dsigmoid(y):
  return 1 - y**2

def matr( I, J, fill=0.0):
  m = []
  for i in range(I):
    m.append([fill]*J)
  return m

def randMatr( matrix, a, b):
  for i in range( len(matrix) ):
    for j in range( len(matrix[0]) ):
      matrix[i][j] = random.uniform(a,b)

def main():
  patron = [ [[0,0], [1]], [[0,1], [1]], [[1,0], [1]], [[1,1], [0]]  ]
  RED = red( 2, 2, 1)
  RED.entrena(patron)


if(__name__ ==  '__main__'):
    main()
