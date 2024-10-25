import numpy as np
from random import *
l=[12,3,3,3,4,4,4]
a=np.array(l)
print(a)
print(a[::-1])
print(a.astype(float))
a=np.arange(2,11).reshape((3,3))
print(a)
a=np.zeros(10)
print(a)
print(a)
a=np.empty((3,3))
print(a)
a=np.full((3,3),5)
print(a)
l=[0, 12, 45.21, 34, 99.91]
a=np.array(l)
print(a*5)
a=np.random.randint(10, size=(10))
b=np.random.randint(10, size=(10))
l=[]
l1=[]
l2=[]
for i in a:
    if i in b:
        l.append(True)
        l1.append(i)
    else:
        l.append(False)
        l2.append(i)
            
print(a,np.unique(a),b,l,l1, sorted(l2))
print(np.in1d(a,b),np.intersect1d(a,b))
print(np.all(a), np.any(b))
print(a<b)
print(a[a>3], np.nonzero(a>3))
a=np.ones((2,2), float)
a=np.arange(2,14).reshape((4,3))
print(a, a.reshape(2,6), np.ravel(a))
a=np.full((3,5),2, dtype=np.int)
print(a)
#a=np.zeros((4,4))
a=np.diag([2,4,6,8])
print(a)
a=np.arange(2.5,6.55, 4/30, float)
print("rrrrrrrrrr",a)
a=np.arange(2,14).reshape((4,3))
print(np.triu(a,1))
b=a[2,:]
b[[0,]]=0
b=a[3,:]
b[[0,1]]=0
print(a)
a=np.tri(4,3,-2)
print(a)
print(a.flat[8])
a=np.zeros((3,2))
print(np.moveaxis(a,-1,0).shape)
n=12
print(type(n))
print(np.arange(0,n).reshape(3, int(n/3)))
x = np.zeros((3, 4))
y = np.expand_dims(x, axis=0).shape
print(y)

x = np.arange(1, 15)
print(np.split(x, [2, 3,9]))
a=np.arange(0,16).reshape(4,4)
print(np.split(a, [2], axis=1))
a=np.full((5,5),2)
a[:]=[1,2,3,4,5]
print(a)
print(np.linspace(0,1,12, endpoint=True)[1:-1])
#print(np.arange(0,10**3, dtype=float))
a=np.ones((5,5,5))
#print(a)
a=np.arange(12).reshape(3,4)
print(a**3)
print(np.split(a, [1,2,3], axis=1))

import numpy as np
x= np.arange(6).reshape(3, 2)
print(x)
print(x.tolist())
print(x.tolist()[1], x[:,0], x[1,:])
print(np.array([i for i in range(10)]))
a=np.arange(10,70,10).reshape(2,3)
print(np.append(a,[[100],[200]], axis=1))
x = np.array([[20, 20, 20, 0],
              [0, 20, 20, 20],
              [0, 20, 20, 20],
              [20, 20, 20, 0],
              [10, 20, 20,20]])
print("Original array:")
print(x)
y = np.ascontiguousarray(x).view(np.dtype((np.void, x.dtype.itemsize * x.shape[1])))
print(y)
_, idx = np.unique(y, return_index=True)
print(idx)
unique_result = x[idx]
print(unique_result)
x = np.array([-1,-4,0, 2, 3, 4, 5, -6])
x[x<0]=0
print(x)
a = np.array( [10,10,20,10,20,20,20,30, 30,50,40,40] )
unique_elements, counts_elements = np.unique(a, return_counts=True)
print(np.asarray((unique_elements, counts_elements)))
a= np.array([97, 101, 105, 111, 117])
b = np.array(['a','e','i','o','u'])
print(a)
print(b)
print(b[(100 < a) & (a < 110)])
a= np.array([[20, 20, 20],
[30, 30, 30],
[40, 40, 40]])
print(sum(a), a.prod())
print(np.ones((3,3)))
print(a[:,0])
a= np.array([97, 101, 105, 111, 117])
x= np.array([0,0])
a.put([0,4],x)

"""
from PIL import Image
import numpy as np
img_w, img_h = 200, 200
data = np.zeros((img_h, img_w, 3), dtype=np.uint8)
data[100, 100] = [255, 0, 0]
img = Image.fromarray(data, 'RGB')
img.save('test.png')
#img.show()
"""
print(a)
x = np.array([-1,6])
y = np.array([-1])
a= np.transpose([np.tile(x, len(y)), np.repeat(y, len(x))])
print(a)


a=np.array([1, 0, 2, 0, 3, 0, 4, 5, 6, 7, 8])
print(np.where(a==0)[0],a[a]>a)
a=np.empty((0,3), int)
print(a)
a=np.append(a,[[10,20,30]], axis=0)
a=np.append(a,[[10,20,30]], axis=0)
print(a)
i,j = np.unravel_index(a.argmax(), a.shape)
print(a[i,j])
print(a[[0,1],[0,2]])
a=np.arange(9).reshape(3,3)
b=np.array([11,12,13])
c=np.array([[0],[10],[20]])
print(a+b)
print(c+b)
print(np.resize(a,(2,2)))
z=np.resize(a,(4,5))
print(z, "**", np.resize(z,(5,4)))

a=np.arange(9).reshape(3,3)
a1=np.arange(10,19).reshape(3,3)
print(np.hstack((a,a1)))
print(np.vstack((a,a1)))
print(np.split(a, [0,1,2], axis=1))
print(a.size, a.ndim, a.itemsize)
a=np.arange(16).reshape(4,4)
print(a)
print(a[0,:], a[:,2])
print(a[0:2,0:2], a[1::2,0::2])
print(a[[1,3],[0,3]])
print("--------")
a=np.arange(36).reshape(6,6)
print(a[2::2,0::2])
b=a.copy()
print(b)
array = np.array([24, 27, 30, 29, 18, 14])
print("Original array:")
print(array)
argsort_array = array.argsort()
print(argsort_array)
ranks_array = np.empty_like(argsort_array)
print(ranks_array)
ranks_array[argsort_array] = np.arange(len(array))
print(ranks_array)
print(sum(a[0:5,:]))
