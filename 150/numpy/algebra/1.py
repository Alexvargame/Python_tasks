import numpy as np
from random import *
a = np.arange(4).reshape(2,2)
a1=np.arange(5,9).reshape(2,2)
print(a)
print(a1)
for i in range(len(a)):
    for j in range(len(a1)):
        print(sum(a[j,:]*a1[:,i]))
print(np.dot(a,a1))
print(np.linalg.det(a))
print(np.dot(a,np.linalg.inv(a)))
