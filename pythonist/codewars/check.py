from itertools import combinations
from math import sqrt
from functools import reduce


                   

def check(astr):
    ast=astr[0]
    res=[]
    l=0
    for i in range(1,len(astr)):
        if astr[i] in ast:
            ind=ast.index(astr[i])
            print('1',i,astr[i],ast,ind, ast[ind:])
            input()
            
            res.append(ast)
            if len(ast)>l:
                l=len(ast)
            ast=ast[ind+1:]+astr[i]
            print('2',ast)
        else:
            ast=ast+astr[i]
            print('3',ast)
            input()
    if len(ast)>l:
        l=len(ast)
    res.append(ast)   
    print(res)   
    
    return l
                   
                                                    
def main():

   
    print(check('abcabrtrwcbbasrtw'))
    
    


   


if __name__ == "__main__":
    main()

