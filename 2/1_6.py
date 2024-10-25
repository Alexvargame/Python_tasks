dict1={'one':1,'two':2,'three':3}
print(dict1)
dict1['four']=4
print(dict1)
dict1[('five','five')]=[5,5]
print(dict1)
print(dict1['one'])
dict1.pop('two')
print(dict1)
for i in dict1:
    print (i)
