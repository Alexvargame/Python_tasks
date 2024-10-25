import math
data=['Name', 'Age', 'Adress']
for i in data:
    print(str(i))
print("(x + y) * (x + y)")
x=4
y=3
print("res:", (x+y)**2)

amt = 10000
int_ = 3.5
year = 7
for i in range(7*12):
    amt=amt+amt*int_/1200
print(amt)

x1=int(input("x1:", ))
x2=int(input("x2:", ))
y1=int(input("y1:", ))
y2=int(input("y2:", ))

print("distance:", math.sqrt((x2-x1)**2+(y2-y1)**2))
