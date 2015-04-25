import theano.tensor as T
import theano.tensor as T
import numpy as np
import theano
# x,y, z are symbolic variables, they represent relationships
x = T.scalar()
y = T.scalar()
z = x + y
# Compiles a function ftnSum (Reusable), actual C compilation, automatically cares about parallism
ftnSum = theano.function(inputs=[x,y], outputs=z)
print(ftnSum(3,4))
