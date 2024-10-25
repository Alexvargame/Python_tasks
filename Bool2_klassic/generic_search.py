from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set,Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop
from time import *
T= TypeVar('T')
def linear_contains(iterable, key):
    t=time()
    for item in iterable:
        if item == key:
            return time()-t 
    return False
С = TypeVar("C", bound="Comparable")
class Comparable(Protocol):
    def __eq__(self,other):
        pass
    def __lt__(self,other):
        pass
    def __gt__(self, other):
        return (not self < other) and self != other
    def __le__(self, other):
        return self<other or self == other
    def __ge__(self, other):
        return not self < other 

def binary_contains(sequence, key):
    low: int = 0
    high: int = len(sequence) - 1
    t=time()
    while low <= high: #пока еще есть место для поиска
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return time()-t
    return False

class Stack(Generic[T]):
    def __init__(self):
        self._container=[]
    @property
    def empty(self):
        return not self._container
    def push(self, item):
        self._container.append(item)
    def pop(self):
        return self._container.pop()
    def __repr__(self):
        return repr(self._container)


class Queue(Generic[T]):
    def __init__(self):
        self._container=Deque()
    @property
    def empty(self):
        return not self._container
    def push(self, item):
        self._container.append(item)
    def pop(self):
        return self._container.popleft()
    def __repr__(self):
        return repr(self._container)

class PriorityQueue(Generic[T]):
    def __init__(self):
        self._container=[]
    @property
    def empty(self):
        return not self._container
    def push(self, item):
        return heappush(self._container,item)
    def pop(self):
        return heappop(self._container)
    def __repr__(self):
        return repr(self._container)


class Node(Generic[T]):
    def __init__(self, state, parent, cost=0.0,heuristic=0.0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic

    def __lt__(self,other):
        return self.cost+self.heuristic

def dfs(initial, goal_test, successors):
    frontier=Stack()
    frontier.push(Node(initial, None))
    explored={initial}

    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None

def bfs(initial, goal_test, successors):
    frontier=Queue()
    frontier.push(Node(initial, None))
    explored={initial}

    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None

def astar(initial, goal_test, successors,heuristic):
    frontier=PriorityQueue()
    frontier.push(Node(initial, None,0.0,heuristic(initial)))
    explored={initial:0.0}

    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.state
        if goal_test(current_state):
            
            return current_node
        for child in successors(current_state):
            new_cost= current_node.cost + 1

            if child not in explored or explored[child]>new_cost:
                explored[child]=new_cost
                frontier.push(Node(child, current_node,new_cost,heuristic(child)))
    return None

def node_to_path(node):
    path=[node.state]
    while node.parent is not None:
        node=node.parent
        path.append(node.state)
    path.reverse()
    return path


        
if __name__=="__main__":
    
    print(linear_contains([i*i for i in range(1000000)], 14888**2))
    print(binary_contains([i*i for i in range(1000000)], 14888**2))
    


