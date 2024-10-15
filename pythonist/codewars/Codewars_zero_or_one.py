
from math import sqrt
from functools import reduce

def zero_or_one(n,s):
    return [1 if sum(list(zip(*s))[i])>n/2 else 0 for i in range(len(s[0]))]

                   
                                                    
def main():
   
    
    #print(zero_or_one(3,[[1,1,0], [1,0,0], [0,1,1]]))
    print(zero_or_one(1,[[1,1,0,1]]))
        
    
    


   


if __name__ == "__main__":
    main()

