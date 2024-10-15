from itertools import combinations
from math import sqrt


def compare(a,b):
    astr=''.join([x for x,y in zip(a,b) if x==y])
##    astr=''
##    for i in range(min(len(a),len(b))):
##        if a[i]!=b[i]:
##            return astr
##        astr=astr+a[i]
    return astr
            
                   

def prefix(alst):
    astr=alst[0]
    for i in range(1,len(alst)):
        astr=compare(alst[i],astr)
        
  
    return astr
                   
                                                    
def main():

   
    print(prefix(['дом', 'домен', 'домра', 'доширак']))
    


   


if __name__ == "__main__":
    main()

