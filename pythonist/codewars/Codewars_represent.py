from itertools import permutations
from math import sqrt, factorial

def represent(n):
##    result=[item for item in permutations([i*(i+1)/2 for i in range(int(sqrt(n))*2)],3) if sum(item)==n]
##
##    for item in permutations([i*(i+1)/2 for i in range(int(sqrt(n))*2)],3):
##        if sum(item)==n:
##            return [int(i) for i in item]
    al=[i*(i+1)/2 for i in range(int(sqrt(n))*2)]
    for i in range(len(al)):
        for j in range(i,len(al)):
            #for k in range(j,len(al)):
                if int(al[i])+int(al[j])==n:
                    return [int(al[i]),int(al[j])]
    #return result  
    
def main():
    print(represent(1000000))

       
if __name__ == "__main__":
    main()
