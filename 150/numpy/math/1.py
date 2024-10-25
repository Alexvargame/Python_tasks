import numpy as np
from random import *
a = np.array([[10,40],[30,20]])
print(a)
print(np.sort(a, axis=0))
print(np.sort(a))
print(np.sort(a, axis=None))
data_type=[('name', 'S15'), ('class', int), ('height', float)]
students_details=[('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
stud=np.array(students_details, dtype=data_type)
print(stud)
print(np.sort(stud, order=('class', 'height') ))
b=np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
indexx=np.argsort(b)
print(indexx)

nums = np.array([70, 50, 20, 30, -11, 60, 50, 40])
print("Original array:")
print(nums)
print("\nAfter partitioning on 4 the position:")
print(np.partition(nums, 5))
               
