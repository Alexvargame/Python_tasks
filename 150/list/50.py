lst= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l ',' m ',' n ']
lst1=[]
n=3
for j in range(n):
    lst1.append([])
    for i in range(j, len(lst),n):
        lst1[j].append(lst[i])
print(lst1)
print("_______________________")

lst=["красный", "оранжевый", "зеленый", "синий", "белый"]
lst1=["черный", "желтый", "зеленый", "синий"]

def razn(l, l1):
    lst2=[]
    for i in l:
        if i not in l1:
            lst2.append(i)
    return lst2

print(razn(lst, lst1))
print(razn(lst1, lst))
print("""""""__________")

print(('').join(lst))
for i in lst:
    print(i, end=" ")
print()
str1="col_"
print("--------------")
for i in lst:
    i=str1+str(i)
    print(i, end=" ")
    

    
