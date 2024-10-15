
from math import sqrt
from functools import reduce

def runoff_voting(voting):

    for vv in range(len(voting[0])):

        
        
        
        if len(set(list(zip(*voting))[0]))==1:
            print('!')
            return list(zip(*voting))[0][0]
        elif len(set(list(zip(*voting))[0]))==len(list(zip(*voting))[0]) or len(set([list(zip(*voting))[0].count(i) for i in list(zip(*voting))[0]]))==1:
            print('!')
            return None
        else:

            v=[i for i in list(zip(*voting))[0] if
                  list(zip(*voting))[0].count(i)==min([list(zip(*voting))[0].count(i) for i in list(zip(*voting))[0]])]
            if len(set(v))==len(set(list(zip(*voting))[0]))-1:
                return [vv for vv in list(zip(*voting))[0] if vv not in v][0]

            print(v)
            voting=[[i for i in vot if i not in v ] for vot in voting]
            print(voting)
            input()
            if not voting[0]:
                return None
    
    
   

                   
                                                    
def main():
   
    
##    print(runoff_voting([["dem", "ind", "rep"],
##                  ["rep", "ind", "dem"],
##                  ["ind", "dem", "rep"],
##                  ["ind", "rep", "dem"]]))
        
    print(runoff_voting([['Frank Underwood', 'Gihren Zabi', 'Reinhard von Musel', 'Daisuke Aramaki'],
                         ['Daisuke Aramaki', 'Gihren Zabi', 'Frank Underwood', 'Reinhard von Musel'],
                         ['Frank Underwood', 'Reinhard von Musel', 'Gihren Zabi', 'Daisuke Aramaki'],
                         ['Reinhard von Musel', 'Gihren Zabi', 'Daisuke Aramaki', 'Frank Underwood']]))
    


   


if __name__ == "__main__":
    main()

