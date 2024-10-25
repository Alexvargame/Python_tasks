from typing import TypeVar,Generic,List
from heapq import heappop,heappush

T=TypeVar('T')
class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container=[]
    @property
    def empty(self):
        return not self._container
    def push(self,item):
        heappush(self._container,item)
    def pop(self):
        return heappop(self._container)
    def __repr__(self):
        return repr(self._container)

def main():
    pass

if __name__=="__main__":
    main()
