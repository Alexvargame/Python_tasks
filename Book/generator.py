# R-

def names():
 yield "Федор"
 yield "Щарик"
 yield "Кот"
def colors():
 L=["Красный","Желтый","Зеленый","Синий"]
 for clr in L:
     yield clr
def myrange(n):
 for k in range(n):
     yield 2*k+1
print("")
for name in names():
 print(name)
print(list(names()))
R=colors()
print("")
for r in R:
 print(r, end=" ")
print("\nLW")
for r in R:
 print(r, end=" ")
print("E")
print("E:")
print(list(myrange(10)))
print(tuple(myrange(10)))
N=myrange(8)
A=list(N)
print("A =", A)
B=list(N)
print("B =", B)
for num in myrange(8):
 print(num, end=" ")
print()
