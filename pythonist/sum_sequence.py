
from collections import Counter
   

def sum_sequence(a,b,dif):

        if a>b:
                return 0
        else:
                return sum([i for i in range(a,b+dif,dif) if i<b+1])
                

         
        
        
def main():
        
        print(sum_sequence(3,2,2))
        print(sum_sequence(2,2,2))
        print(sum_sequence(2,6,2))
        print(sum_sequence(1,5,1))
        print(sum_sequence(1,5,3))
if __name__ == "__main__":
    main()


