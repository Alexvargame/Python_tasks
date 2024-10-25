import numpy as np
from random import *
a = np.arange(12).reshape((2,6))
print(a)
print(np.max(a, axis=1)-np.min(a,axis=1))
#print(np.ndarray(a,axis=1))

x = np.arange(12).reshape((2, 6))
print("\nOriginal array:")
print(x)
r1 = np.percentile(x, 80, 1)
print("\n80th percentile for all elements of the said array along the second axis:")
print(r1)
