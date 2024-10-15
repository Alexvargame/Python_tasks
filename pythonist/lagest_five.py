
from functools import reduce
from collections import deque

def lagest_five(astr):
    
        return reduce(lambda a,b: a if int(a)>int(b) else b,[astr[i:i+5] for i in range(len(astr)-4)])
    



def main():
         
     
     print(lagest_five('1234567890'))
     print(lagest_five('1234567893523495346'))




if __name__ == "__main__":
    main()


