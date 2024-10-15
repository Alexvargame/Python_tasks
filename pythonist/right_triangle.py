#https://pythonist.ru/yavlyaetsya-li-treugolnik-pryamougolnym/
from functools import reduce
from collections import deque

def right_triangle(x,y,z):

    lt=sorted([x,y,z])
    g=lt.pop()
    
    
    
    return reduce(lambda x,y:x+y,[i**2 for i in lt])==g**2
    









def main():
  
     print(right_triangle(3,5,4))
    


if __name__ == "__main__":
    main()


