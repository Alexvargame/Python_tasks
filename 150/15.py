r=int(input("r:",))
V=r**3*3.14*4/3
print(V)
rr=int(input("r:",))
if 100<rr<1000:
    print("100-1000")
elif 1000<rr<2000:
    print("1000-2000")
else: print("None")

a=int(input("a:",))
b=int(input("b:",))
c=int(input("c:",))
if a==b and a==c:
    print(9*a)
else: print(a+b+c)
