from math import gcd, sqrt
from functools import reduce
import time
# def isPrime(k,alst):
#     if k==2 or k==3 : return True
#     if k%2==0 or k<2 or k%3==0 :return False
#     for i in range(2,len(alst)):
#         if k%alst[i]==0:
#             return False
#     return True

def get_lst_primes(n):
    size = n//2
    lst = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if lst[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            lst[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(lst) if v and i>0]

def sum_for_list(lst):

    lst1=sorted([abs(i) for i in lst],key=abs)
    #lst1.insert(0,2)
    #print(lst,lst1)

    primes=get_lst_primes(lst1[-1]+1)
    tt = time.time()
    res=list([i, reduce(lambda x, y: x + y, list(p for p in lst if  p % i == 0))] for i in primes if
         len([p for p in lst if p % i == 0]))
    ttt = time.time()
    print(ttt - tt)
    # tt = time.time()
    # res=[]
    # for p in lst:
    #     for i in primes:
    #         if abs(p)>i and p % i == 0:
    #             res.append([i, reduce(lambda x, y: x + y, list(p for p in lst if p % i == 0))])
    # ttt = time.time()
    # print(ttt - tt)
    return res
        #list([i, reduce(lambda x, y: x + y, list(p for p in lst if p % i == 0))] for i in primes if
         #len([p for p in lst if p % i == 0])))

#
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
#



def main():
    print(sum_for_list([761477, -805983, -73776, -425176, -52087, 107753, -747576, -370045, -370690, -885629, 466760, -576758, -148034, -872573, -243738]))
    
    # print(sum_for_list([476810, -350656, -412154, -173849, -262944, 632860, -386737, -495760, -707636, -417344, 66522, -524379, -670212, -406682]))
    #print(sum_for_list([448785, -827814, -482555, -406373, -329002, 392637, -813491, -604178, -732580, -926338]))
   
  
  
  
 
if __name__ == "__main__":
    main()


###

