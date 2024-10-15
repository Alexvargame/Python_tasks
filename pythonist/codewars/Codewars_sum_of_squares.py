from math import sqrt
from itertools import combinations_with_replacement, accumulate
def sum_of_squares(n):
    rep=2
    
    if n<0:
        return 0
    if n%sqrt(n)==0:
        return 1
    
    coins=[i**2 for i in range(1,round(sqrt(n))+1)]
    print(coins)
    
    while rep<n:
        print('rep',rep)
        if [item for item in reversed(list(combinations_with_replacement(coins,rep))) if sum(item)==n]:
            print([item for item in combinations_with_replacement(coins,rep) if sum(item)==n])
            return rep
        rep=rep +1

            
                                       
##    print([len(items) for sublist in [[item for item in combinations_with_replacement(coins,rep) if sum(item)==n]
##           for rep in range(n) if len([item for item in combinations_with_replacement(coins,rep) if sum(item)==n])>0] for items in sublist])
##    return min([len(items) for sublist in [[item for item in combinations_with_replacement(coins,rep) if sum(item)==n]
##           for rep in range(n) if len([item for item in combinations_with_replacement(coins,rep) if sum(item)==n])>0] for items in sublist])
##

def main():


    print(sum_of_squares(39999))
   
  
  
  
 
if __name__ == "__main__":
    main()


###
