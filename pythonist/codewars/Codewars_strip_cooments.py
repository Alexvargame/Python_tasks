from itertools import permutations
from math import sqrt
from functools import reduce
import re

                   

def strip_comments(lst):
   

    return [''.join(item) for item in permutations(lst,6)]
   
                   
                                                    
def main():

   
    print(strip_comments(['а','р','д','ы','л','к']))

    
    


   


if __name__ == "__main__":
    main()

