class A:
    def __init__(self, a):
        self.a=a
    def show(self):
        print(self.a)
class B(A):
    def __int__(self,b):
        self.b=b
    
a=A(1)
a.show()
b=B(2)
print(b.a)
b.show()
print("-----------")

class AType:
    def __init__(self,a):
        self.a=a
    def show(self):
        if type(self.a)==int:
            print(self.a**2)
        elif type(self.a)==float:
            print(self.a*2)
        elif type(self.a)==str:
            print(self.a)
a=AType("aasf")
b=AType(5.1)
c=AType(2)
a.show()
b.show()
c.show()
        
class lisst:
    def __init__(self, l):
        self.l=l
    def add_(self, cl):
        li=[]
        li.extend(self.l)
        li.extend(cl.l)
        c=lisst(li)
        return c
    def compire(self, cl):
        for i in range(max(len(self.l), len(cl.l))):
            if not self.l[i]:
                self.l[i]=0
            elif not cl.l[i]:
                cl.l[i]=0
            if self.l[i]>cl.l[i]:
                return "self.l+ bigger"
            elif self.l[i]<cl.l[i]:
                return "cl.l+ bigger"
        return self.l+" equil "+cl.l
                       
a=lisst([3,2])
b=lisst([3,1,5])
print(a.add_(b).l)
print(a.compire(b))
print("----------------")

class oper:
    def __init__(self, num):
        self.num=num
    def add(self,n):
        print(self.num+n)
    def prod(self,n):
        print(self.num*n)
    def minus(self,n):
        print(self.num-n)
    def delen(self,n):
        print(self.num/n)
    def show(self):
        print(self.num)
x=oper(10)
x.show()
x.add(1)
x.prod(4)
x.minus(3)
x.delen(2)
print("--------------")
