import numpy as np
from random import *
a = np.random.randint(10,30,(5))
print(a)
a=np.random.random((3,3,3))
print(a)
print(a.max(), a.min())
a=np.random.random((10,4))
print(a)
print(a[0:5,:])
a=np.random.randint(1,10,(10))
print(a)
print(np.random.permutation(10))
a=np.random.random(15)
print(a)
a[a.argmax()]=-1
print(a)
print("--------")
a=np.random.random((10,2))
print(a)
x,y = np.atleast_2d(a[:,0], a[:,1])
print("x", x)
print("y",y)
d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
print(d)