from functools import wraps
from time import time
from collections import Counter
from math import *



def valid_subset(l_1, l_2):
    rcnt=Counter(str(l_1))
    for rk, rv in rcnt.items():
        try:
            if int(rk) in l_2:
                continue
            else:
                return False
        except ValueError:
            pass
        
    return True

def main():
    print(valid_subset([[1,2],[3],[1,0,9]], [1,3,2,9,0]))
    print(valid_subset([[1,2],[3],[1,0,9]], [1,3,2,0]))
    print(valid_subset([[1,2],[3],[1,0,9]], []))
    print(valid_subset([[1,2],[],[1,0,9]], [1,3,2,9,0]))
    print(valid_subset([[1,2],[],[1,0,9]], []))
    print("Тестовые")
    print(valid_subset([[1,2],[2,3],[1,3]], [1,3,2]))
    print(valid_subset([[1,2],[2],[3],[]], [1,3,2]))
    print(valid_subset([[1,2],[2,3],[1,4]], [1,3,2]))
    print(valid_subset([[1,2,3,4]], [1,3,2]))
    

    
 

if __name__ == "__main__":
    main()


