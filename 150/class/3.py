class skobki():
    def __init__(self, str_):
        self.str_=str_
        
        self.sk=[('(',')'),('[',']'),('{','}')]

    
    def eq(self):
        for i in range(len(self.str_)-1):
            for j in range(len(self.sk)):
                if self.str_[i]==self.sk[j][0] and self.str_[i+1]==self.sk[j][1] :
                        print(self.str_[i], self.str_[i+1])
                    
            
skobki('[]').eq()
print("___")
from random import *
class nabor():
    def __init__(self,n):
        
        self.n=n
        

    def list_(self):
        l=[randint(0,10) for i in range(self.n) ]
  
print(nabor(3).list_())
class nabor1():
    def __init__(self,m,n):
        self.m=m
        self.n=n
        

    def list_(self):
       l=[randint(0,10) for i in range(self.n) ]
       return l

    def combi(self, l):
        
      lst2=[]
    
      for i in range(len(l)):
       for j in range(len(l)):
             if l[i]+l[j]==self.m:
                t=(l[i],l[j])
                lst2.append(t)
      return lst2

print(nabor1(6,10).list_())
print(nabor1(6,10).combi(nabor1(2,7).list_()))
t=nabor1(6,10).list_()
print(nabor1(6,10).combi(t))
