from datetime import *
import random

class one:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a, self.b)
a=one(1,2)
b=one(3,4)
a.show()

class two:
    def __init__(self, a, b):
            self.a=a
            self.b=b
    def set(self):
        if type(self.a)==int and type(self.b)==int:
            self.a=self.a+self.b
            self.b=None
        elif type(self.a)==str and type(self.b)==str:
            self.a=self.a+self.b
            self.b=None
        else:
            self.a=None
            self.b=None
    def show(self):
        print(self.a, self.b)
a=two(2,4)
a.show()
b=two('a','b')
c=two('a',2)
a.set()
a.show()
b.set()
b.show()
c.set()
c.show()
print(a.a, b.a, c.a)


l=[1,4,'a','r',9,True]
class slist:
    def __init__(self, l):
        self.l=[i for i in l if type(i)==int]
    def show(self):
        for i in self.l:
            print(i)
    def avg(self):
        return sum(self.l)/len(self.l)
s=slist(l)
s.show()
print(s.avg())

l1=['a', 'b','c']
vals=[1,2,3]
def list_cl(txt, l1, vals):
    class Me:
        def __init__(self):
            k=0
            for i in l1:
                if type(i)==str:
                    self.__dict__[i]=vals[k]
                    #print(__dict__[i])
                    k=k+1
    Me.__name__=txt
    return Me()
aa=list_cl('N', l1, vals)
print(aa)

def l_cl(aa):

    b=aa
    for i in aa.__dict__:
        if type(aa.__dict__[i])==int:
            b.__dict__[i]=i
            print(b.__dict__[i])
l_cl(aa)


def cl_li(n):
    cl_l=[]
    l1=['a', 'b','c']
    vals=[1,2,3]
    txt='MyClass'
    for j in range(n):
        
        class Me:
            def __init__(self):
                k=0
                for i in l1:
                    if type(i)==str:
                        self.__dict__[i]=vals[k]
                        k=k+1
        Me.__name__=txt
        cl_l.append(Me())
    return cl_l

print(cl_li(3))
print("________________-----")
class A:
    def __init__(self, l):
        self.l=l
    def show(self):
        for i in self.l:
            print(i, end=' ')

a1=A([1,2,3])
a2=A([2,4,5])
a1.show()
print()
def s(a1,a2):
    ll=[]
    for i in range(len(a1.l)):
        ll.append(a1.l[i]+a2.l[i])
    a3=A(ll)
    return a3
s(a1,a2).show()

class Chain:
    def __init__(self, name, n=1):
        self.name=name
        if n==1:
            self.next=None
        else:
            self.next=Chain(self.name, n-1)
        self.set()
    def set(self, num=1):
        self.code=self.name+"["+str(num)+"]"
        if self.next!=None:
             self.next.set(num+1)
    def show(self):
        print(self.code)
        if self.next!=None:
            self.next.show()
    
        
def chain(c):
    A=Chain("A")
    A.show()
    B=Chain("B",3)
    B.show()
chain(Chain)
print()

class Tree:
    def __init__(self, name, n=1):
        self.name=name
        if n==1:
            self.next=None
        else:
            self.next=Tree(self.name, n-1)
        self.set() 
        #self.set_left()
        #self.set_right()
    def set(self, n=1):
        self.code=self.name+"["+str(n)+"]"
        self.code_left=self.name+"["+str(n+1)+"]"
        self.code_right=self.name+"["+str(n+2)+"]"
        if self.next!=None:
             self.next.set(n+2)
    def set_left(self, n=1):
        self.code_left=self.name+"["+str(n+1)+"]"
       
        
    def set_right(self, n=1):
        self.code_right=self.name+"["+str(n+2)+"]"
        
    def show(self):
        print(self.code, self.code_left, self.code_right)
        if self.next!=None:
            self.next.show()
A=Tree("A",5)

A.show()
class S:
    def __init__(self, l):
        self.l=[]
        if type(l)==list:
            
            self.set(l)
        else: print("rrr")

    def set(self, l):
        for i in l:
            if type(i)==str:
                self.l.append(i)
    def show(self):
        for i in range(len(self.l)):
            print(self.l[i][0])
a=S(5)
a=S([1,2,'dsdsd'])
a.show()
class Alpha:
 

 def __getitem__(self, index):
     
     return self.value[index][0]

 def __setitem__(self, index, val):
     self.value[index]=val
 
 def __delitem__(self, index):
     del self.value[index]

 def __str__(self):
     return str(self.value)

 def __len__(self):
     return len(self.value)
A=Alpha()
A.value=[[1,2],[3,4]]
print(A[1])

class AA:
    def __call__(self, n, x):
        s=0
        for i in range(len(self.nums)):
            s+=self.nums[i]*x**i
        return s

A=AA()
A.nums=[1,2,3]
print(A(2,3))
print("--------")
class AL:
    def __init__(self, vals):
        L=[1,1]
        for i in range(1,vals):
            L.append(L[i]+L[i-1])
        self.digits=L
        self.position=-1

    def __iter__(self):
        return self
    def __next__(self):
        self.position+=1
        
        if self.position<len(self.digits):
            
            return self.digits[self.position]
        else:
            raise StopIteration

        
A=AL(10)
print(next(A))
for s in A:
    print(s)
    
