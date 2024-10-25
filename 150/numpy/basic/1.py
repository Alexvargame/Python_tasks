import numpy as np
from random import *
"""
l= [1,1,np.inf,2]
a=np.array([l])
#print(a)
#print(np.any(a))
#print(np.isfinite(a))

#print (a.dtype, a.astype(np.int))
#print(np.indices((4,4)))
m=np.random.rand(3,3)
#print(m)
#print(np.random.randint(1,3,size=(3,3)))
#print(np.random.choice([1,2],size=(3,3)))
#print(a.reshape((2,2)))
#print(a.ravel('A'))
#print(a.ravel('C'))
#print(m[1][1], m[[1]], m[[0,1],[0,0]])
a = np.random.randint(3,size=(3,4))
#print(a)
#print(a[1], a[-2])
#print(a[[1,2]])
#print(a[np.array([1,2])])
#print(a[np.array([0,2,1])])
x = np.arange(12).reshape(3,4)
print(x)
y=x[0,[0,1,2,3]]
print(y, y[[0,1,2]])
y[[0,1,2]]=99
print(x)
y=x[1,:]
y[[0,1,2]]=99
print(x)
x = np.arange(12).reshape(3,4)
x[[1,2],[False,True,True,False]] = 99
print(x)

a = np.random.randint(10,size=(3,4))
b = np.random.randint(10,size=(3,4))
print(a)
print(b)
print(np.all(a, axis=1))
print(np.apply_along_axis(lambda x: sum(x), axis=1, arr=a))
print(np.argmax(a), np.argmin(a), np.argmax(a, axis=0))
print(a+b)
print(a*b)
print(np.power(a,b))

a = np.array([0.0, 10.0, 20.0, 30.0]).reshape(-1,1)
b = np.array([1.0, 2.0, 3.0])
print(a+b)
print (a.shape,b.shape)
print(a+b)
def triangle_wave(x,c,c0,hc):
    x = x - int(x)   # Период равен 1, рассчитать с дробной частью
    if x>=c:
        r = 0.0
    elif x<c0:
        r = x/c0*hc
    else:
        r = (c-x)/(c-c0)*hc
    return r

triangle_wave_ufunc = np.frompyfunc(triangle_wave,4,1)
x = np.arange(10)/10.
y2 = triangle_wave_ufunc(x,0.6,0.4,1.0)
# Пользовательский ufunc возвращает тип элемента массива - object, поэтому вам также необходимо вызвать функцию преобразования типов
y2.astype(float)
"""

print(np.arange(15,55,5, dtype=int))
a = np.random.randint(10,size=(3,4))
for i in np.nditer(a):
    print(i)
a = np.arange(20)
print(a)
a[(a>9)&(a<15)]*=-1
print(a)
a = np.random.randint(10, size=5)
print(a)
b = np.random.randint(10, size=5)
print(b)
print(a*b)

a = np.arange(10,22).reshape((3,4))
print(a)
print(a.shape)
a = np.eye(3)
print(a)
a = np.zeros((10,10))
print(a)
#a[[1,8],[True,True,True,True,True,True,True,True,True,True]]=1
b=a[0,:]
b[:]=1
b=a[9,:]
b[:]=1
for i in range(1,9):
    b=a[i,:]
    b[[0,9]]=1
print(a)

a = np.zeros((4,4))
print(a)
for i in range(4):
    print(i, (i+1)%2)
    if ((i+1)%2)==1:
        b=a[i,:]
        b[[1,3]]=1
    else:
        b=a[i,:]
        b[[0,2]]=1
print(a)
a = np.random.randint(3,size=(3,3))
print(a, a.sum(), a.sum(axis =0), a.sum(axis = 1))
la =[]
for i in np.nditer(a):
    print(i)
    la.append(int(i))
print(la)
#a = np.arange((la)).reshape((3,3))
print(a)

import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.2)
y = np.sin(x)
print("Plot the points using matplotlib:")
plt.plot(x, y)
plt.show()
