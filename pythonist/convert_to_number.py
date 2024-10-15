#https://pythonist.ru/cziklicheskij-sdvig/
from functools import reduce
from collections import deque

def circular_shift(alst,blst,n):

    
    
    return alst == blst[2:]+blst[:2]
    









def main():
  
     print(circular_shift([1, 2, 3, 4], [3, 4, 1, 2], 2))
    


if __name__ == "__main__":
    main()


