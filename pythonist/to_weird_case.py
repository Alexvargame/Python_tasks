
from collections import Counter
   


def to_weird_case(astr):
        print(astr.split())
        return ' '.join([''.join([aastr[i].upper() if i%2==0 else aastr[i].lower() for i in range(len(aastr))]) for aastr in astr.split()])
        
                

         
        
        
def main():
        
        print(to_weird_case('String'))
        print(to_weird_case('Weird string case'))
   
        
if __name__ == "__main__":
    main()


