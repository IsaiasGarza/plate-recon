#Simple TLU

inputs = [1,1]
weights = [1,1]
threshold = 1.5
activation = 0
for i in range( len(inputs) ):
    activation += (inputs[i] * weights[i])
if activation > threshold:
    print 1
else:
    print 0