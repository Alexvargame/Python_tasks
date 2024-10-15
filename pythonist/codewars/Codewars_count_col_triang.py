from itertools import combinations
from math import sqrt

def is_triangle(item):
   
    lst=[sqrt((it[1][0]-it[0][0])**2+(it[1][1]-it[0][1])**2) for it in [it for it in combinations([i[0] for i in item],2)]]

    if sorted(lst)[1]+sorted(lst)[0]>sorted(lst)[2]:
        return True
    return False
    

def count_col_triang(input_):
   
    colors=[a[1] for a in input_]
    colors=list(set([a for a in colors if colors.count(a)>2]))
    blst=[]
    bdict={}
    print(colors)
    print([[a for a in input_ if a[1]==col] for col in colors])
    alst=[[item for item in combinations([a for a in input_ if a[1]==col],3)  if is_triangle(item)] for col in colors]
    print([[item for item in combinations([a for a in input_ if a[1]==col],3) if is_triangle(item)] for col in colors])
  
        
    print("Общее число точек", len(input_))
    print("Кол-вл цветов", len(set([a[1] for a in input_])))
    print("Общее число треугольников", sum(len(a) for a in alst) )
    print(sorted([[aa[0][1] for aa in a ] for a in alst],key=len))
    if len([[aa[0][1] for aa in a ] for a in alst])>1:
        for k in [[aa[0][1] for aa in a ] for a in alst]:
            
            key,value=k[0],len(k)
            
            bdict[key]=value
        print(bdict)
        for key,value in bdict.items():
            if value==max(bdict.values()):
                print(key)
                blst.append(key)
                
        print(blst)
        blst.sort()
        blst.append(max(bdict.values()))    
    #print("Самый частый цвет",sorted([[aa[0][1] for aa in a ] for a in alst],key=len)[-1][0])
    #print("Число теругольников смого частого цвета", len(sorted([[aa[0][1] for aa in a ] for a in alst],key=len)[-1]))
    
    return [len(input_),len(set([a[1] for a in input_])),sum(len(a) for a in alst) ,blst]
                                                    
def main():

   
    print(count_col_triang([[[3, -4], 'blue'], [[-7, -1], 'red'], [[7, -6], 'yellow'],
                            [[2, 5], 'yellow'], [[1, -5], 'red'], [[1, 1], 'red'], [[1, 7], 'red'],
                            [[1, 4], 'red'], [[-3, -5], 'blue'], [[4, 1], 'blue']]))
    


   


if __name__ == "__main__":
    main()

