from typing import TypeVar, Generic,List
T=TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._container=[]

    def push(self,item):
        self._container.append(item)
    def pop(self):
        return self._container.pop()
    def __repr__(self):
        return repr(self._container)

def hanoi(begin,end,temp,n):
    if n==1:
        end.push(begin.pop())
    else:
        hanoi(begin,temp,end,n-1)
        print('1',begin,end,temp)
        hanoi(begin,end,temp,1)
        print('2',begin,end,temp)
        hanoi(temp,end,begin,n-1)
        print('3',begin,end,temp)
        input()

                            


def main():
    
    num_discs=3
    tower_a=Stack()
    tower_b=Stack()
    tower_c=Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i) 
    hanoi(tower_a,tower_b,tower_c,num_discs)
    print(tower_a,tower_b,tower_c)


if __name__=="__main__":

    main()





