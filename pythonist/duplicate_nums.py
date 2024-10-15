from functools import wraps
from time import time
from collections import Counter
from math import *



def duplicate_nums(alst):
    li=[]
    if len(alst)==len(set(alst)):
        return None
    else:
        alstcnt=Counter(alst)
        for ak, av in alstcnt.items():
            if av>2:
                return False
            elif av==2:
                li.append(ak)
        return sorted(li)
    #[item for item in alst if item not in set(alst)]- красиво. но не то
def main():
   
    print("Тестовые")
    print("list:", duplicate_nums([1,2,3,4,3,5,6]))
    print("list:", duplicate_nums([81,72,43,72,81,99,99,100,12,54]))
    print("list:", duplicate_nums([1,2,3,4,5,6,7,8,9,10]))

    
 

if __name__ == "__main__":
    main()


