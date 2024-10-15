#https://pythonist.ru/samoe-dlinnoe-slovo/
from functools import wraps
from time import time
from collections import Counter
from math import *



def validate_spelling(astr):

    lst=astr.split('. ')
    if ('').join(lst[:-1]).capitalize()==lst[-1].strip(',.-&?!'):
        return True
    return False


    
    
def main():
   
    print(validate_spelling("C. Y. T. O. P. L. A. S. M. Cytoplasm?"))
    print(validate_spelling("H. A. N. K. E. R. C. H. E. I. F. Handkerchief."))
    print(validate_spelling("P. H. A. R. A. O. H. Pharaoh!"))    
        
if __name__ == "__main__":
    main()


