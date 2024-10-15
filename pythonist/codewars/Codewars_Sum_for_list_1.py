from math import gcd, sqrt
from functools import reduce
import time
def isPrime(k):
    if k==2 or k==3 : return True
    if k%2==0 or k<2 or k%3==0 :return False
    for j in range(2,int(k/2)+1):
        if k%j==0:
            return False
    return True
    
def sum_for_list(lst):
    res=[]
    max_=int(max([abs(i) for i in lst])/2+1)
    lst_=list(range(max_))+[abs(l) for l in lst if abs(l)>max_]
    for i in lst_:
        if isPrime(i):
            if len([l for l in lst if l%i==0])!=0:
                res.append([i,sum([l for l in lst if l%i==0])])
    return res


def main():
    #print(sum_for_list([945147, -280531, -534623, -55249, -703899, 20127, -133211, -18439]))
    print(sum_for_list([107, 158, 204, 100, 118, 123, 126, 110, 116, 100]))

    # print(sum_for_list([476810, -350656, -412154, -173849, -262944, 632860, -386737, -495760, -707636, -417344, 66522, -524379, -670212, -406682]))
    #print(sum_for_list([448785, -827814, -482555, -406373, -329002, 392637, -813491, -604178, -732580, -926338]))
   
  
  
  
 
if __name__ == "__main__":
    main()


###


#     primes1=[2]
#     lst1=sorted([abs(i) for i in lst],key=abs)
#     lst1.insert(0,2)
#     print(lst,lst1)
#     tt=time.time()
#     for i in range(1,int(lst1[-1]/2)+1,2):#lst1[-1]+1,2):
#             if isPrime(i,primes1):
#                 primes1.append(i)
#     primes1.extend([l for l in lst1 if l > int(lst1[-1] / 2) + 1 and isPrime(l, primes1)])
#     print('TTT',time.time()-tt)
#     print('oooooooooooooo',list(primes1))
#     ttt=time.time()
#     print(list([i, reduce(lambda x, y: x + y, list(p for p in lst if p % i == 0))] for i in primes1 if
#          len([p for p in lst if p % i == 0])))
#     print(time.time()-ttt)
#     return list([i,reduce(lambda x,y:x+y,list(p for p in lst if p%i==0))]  for i in primes1 if len([p for p in lst if p%i==0]))
#                 #in range(abs(max(lst,key=abs))) if isPrime(i)
#                 #and len([p for p in lst if p%i==0])>0)
# #list([i,sum([p for p in lst if p%i==0])]  for i in range(abs(max(lst,key=abs))) if isPrime(i) and len([p for p in lst if p%i==0])>0)
