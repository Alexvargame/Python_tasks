from itertools import permutations
from functools import reduce

##def sums(n):
##    suma=0
##    print(type(n))
##    while n>0:
##        digit=n%10
##        suma=suma+digit
##        n=n//10
##
##    return suma

def sorts(n):

    print(n,sorted(list(str(n))))
    return int(''.join(sorted(list(str(n)))))==n

def find_all(sum_digs,digs):
    

    digits=[1,2,3,4,5,6,7,8,9,0]
    #print([dig for dig in range(pow(10,digs-1),pow(10,digs))])
    
   # temp1=[dig for dig in range(pow(10,digs-1),pow(10,digs)) if sums(dig)==sum_digs ]#and sorts(dig)]
    temp=[dig for dig in range(pow(10,digs-1),pow(10,digs)) if reduce (lambda x,y:int(x)+int(y),list(str(dig)))==sum_digs and sorts(dig)]
    print(temp)
    #print(temp1)
    if not len(temp):
            return []
    return [len(temp),
            min(temp),
            max(temp)]
    #return [item for item in permutations(digits,digs)]# if item==sum_digs]
            
def main():


    print(find_all(10,3))
    #print(find_all(10,3))
    #print(find_all(35,6))
    
  
  
 
if __name__ == "__main__":
    main()


###
