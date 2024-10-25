import numpy as np
from random import *
from datetime import *
import  datetime
a = np.arange(12).reshape((2,6))
print(a)
print(np.max(a, axis=1)-np.min(a,axis=1))
#print(np.ndarray(a,axis=1))
print(np.arange('2021-03','2021-04', dtype='datetime64[D]'))
yesterday=np.datetime64('today', 'D')-np.timedelta64(1,'D')
print(yesterday)
print("Number of days, February, 2016: ")
print(np.datetime64('2016-03-01') - np.datetime64('2016-02-01'))
start = datetime.datetime(2022, 1, 12)
dt_array = np.array([start + datetime.timedelta(hours=i) for i in range(24)])
print(dt_array)
