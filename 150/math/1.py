def sq_trap(a,b,h):
    return ((b-a)/2+a)*h

print(sq_trap(2,4,4))

def cil(r,h):
    v=3.14*r**2*h
    sq=2*3.14*r*h+2*3.14*r**2
    return (v,sq)
print(cil(6,4))
def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])
print(power_base_sum(2, 10))
print(power_base_sum(2, 2))
print("iiioiii")
#l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
def del_(l, k):
    for j in range(l[k]-1,int(len(l)/l[k]*(l[k]-1))+1, l[k]-1):

        l.pop(j)
        k=k+1
    return l
def happy(n):
    l=[]
    for i in range(1,n+1):
        l.append(i)
    
    del_(l,1)

    k=1
    while l[k]<len(l):

        del_(l,k)

        k=k+1
    return l

print(happy(100))
