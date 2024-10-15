
from collections import Counter
   
res=[]

def divisors(n):
        res=[i for i in range(2,n//2+1) if n%i==0]
        if res:
                return res
        else:
                return 0
##        m=n
##        while n>1:
##              if n%(n/2)==0:
##                      print(m,n,n/2,n%(n/2))
##                      res.append(n/2)
##                      res.append(n/(n/2))
##                      print(res)
##                      input()
##                      m=n
##                      print(m)
##                      return divisors(n/2)
##              else:
##                return divisors(n//(n/2))
##        
        
                

         
        
        
def main():
        
        print(divisors(12))
        print(divisors(25))
        print(divisors(13))
        
if __name__ == "__main__":
    main()


