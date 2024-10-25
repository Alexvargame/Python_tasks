import collections
txt='Связанный список представляет собой набор узлов, каждый из которых состоит из ссылки и значения. Узлы объединяются в последовательность, используя их ссылки. Связанные списки могут использоваться для реализации более сложных структур данных, таких как списки, стеки, очереди и ассоциативные массивы.'
lst=txt.split(' ')
print(lst)
lst2=[lst.count(n) for n in lst]
print(lst2)
print(str(list(zip(lst, lst2))))
l=list(txt)
print(type(l))
for i in l:
   lst1=[l.count(i) for i in l]
print(str(list(zip(l,lst1))))
