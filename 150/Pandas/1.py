import pandas as pd
import numpy as np
a=np.arange(9).reshape(3,3)
print(a)
ds = pd.Series([2, 4, 6, 8, 10])
ds1 = pd.Series([2, 4, 6, 8, 10])
print(list(ds))
print(ds.add(ds1))
print(ds*ds1)
ds2={'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
new_ds2=pd.Series(ds2)
print(new_ds2)
print(list(new_ds2))
new_a=pd.DataFrame(data=a)
print(new_a)
#print(new_a.ix[:,1])
print(np.array(ds), type(np.array(ds)))
a1=[1,2,3]
a2=[4,5]
a3=[6]

aaa=pd.Series([a1,a2,a3])
print(aaa)
aaa=aaa.apply(pd.Series).stack().reset_index(drop=True)
print(aaa)
aa=pd.Series([1,4,'t','t',7,'aq',0])
print(aa)
#print(pd.Series(aa).sort_values())
print(aa.append(pd.Series(['455','g'])))
#print(aa[aa<5])
#print(aa[2<aa<4])
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C','D','E'])
print("Original Data Series:")
print(s)
s = s.reindex(index = ['B','A','C','D','E'])
print("Data Series after changing the order of index:")
print(s)
