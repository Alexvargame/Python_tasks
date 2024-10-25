from typing import List, Generic, TypeVar

T=TypeVar('T')

class Stack(Generic[T]):

    def __init__(self):
        self._container=[]
    def push(self, item):
        self._container.append(item)
    def pop(self):
        self._container.pop()
    def __repr__(self):
        return repr(self._container)


num_discs=3

tower_a=Stack()
tower_b=Stack()
tower_c=Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)
  


def hanoi(begin, end, temp, n):
    print(begin, end, temp, n)
    input()
    if n==1:
        print(begin)
        print("$",begin.pop())## пустой?
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp,1)
        hanoi(temp, end, begin, n-1)
        

if __name__== "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)
    
   
