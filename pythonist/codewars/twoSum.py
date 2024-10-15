from itertools import combinations
from math import sqrt



                   

def twoSum(alst,num):
    
    res=[item for item in combinations(alst,2) if sum(item)==num]
  
    return [(alst.index(it[0]),alst.index(it[1])) for it in [item for item in combinations(alst,2) if sum(item)==num]]
                   
                                                    
def main():

   
    print(twoSum([2, 4, 5, 1, 8],5))
    print(twoSum([2, 4, 5, 1, 8],9))
    


   


if __name__ == "__main__":
    main()

