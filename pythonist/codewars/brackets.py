from itertools import combinations
from math import sqrt
from functools import reduce


                   

def brackets(astr):
    br_dict={'(':')','{':'}','[':']'}
    
    res=[]
    for l in astr:
        if l in br_dict.keys():
            res.append(l)
            print(res)
        elif l in br_dict.values():
            
            k=[k for k in br_dict.keys() if br_dict[k]==l][0]
            print(k)
            if k in res:
                res.remove(k)
                print(res)
            else:
                return False
            
        
                
                
    if len(res)==0:
        return True
    return False
                   
                                                    
def main():

   
    print(brackets('(Привет!)(Это){[журнал]}([]код)'))
    
    


   


if __name__ == "__main__":
    main()

