#https://pythonist.ru/raspakovka-vlozhennyh-spiskov/
from collections import Counter
   

def flatten(alst, dept=0):
        count=0
        while len([i for i in alst if type(i)!=list])!=len(alst):#dept>0:
                
                blst=[]
             
                for al in alst:
                        if type(al)!=list:
                                blst.append(al)
                        else:
                                blst.extend(al)
                alst=blst
        
                count=count+1

                
                if dept==count:
                        break
        return alst
        
def main():
 
    print(flatten([1, [2, 3]]))
    input()
    print(flatten([1, [2, [3]]],4))
    input()
    print(flatten([1, [2, [3]]],1))
    input()
    print(flatten([1, [2, [3]]],100))
    input()
    print(flatten([1, [2, [[3]]]],2))
    input()
    print(flatten([1, [2, [[3]]]],1))
    input()
    print(flatten([1, [2, [[3]]]],3))

  
if __name__ == "__main__":
    main()


