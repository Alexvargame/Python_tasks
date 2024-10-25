from __future__ import annotations
from typing import TypeVar, Generic,List
from collections import deque
from heapq import heappop,heappush

T=TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._container=[]
    @property
    def empty(self):
        return not self._container

    def push(self,item):
        self._container.append(item)
    def pop(self):
        return self._container.pop()
    def __repr__(self):
        return repr(self._container)

class Queue(Generic[T]):
    def __init__(self):
        self._container=deque()
    @property
    def empty(self):
        return not self._container

    def push(self,item):
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

    def push(self,item):
        heappush(self._container,item)
    def pop(self):
        return heappop(self._container)
    def __repr__(self):
        return repr(self._container)

class Node(Generic[T]):
    def __init__(self,state,parent,cost=0.0,heuristic=0.0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic
    def __lt__(self,other):
        return (self.cost+self.heuristic)<(other.cost+other.heuristic)


def dfs(initial,goal_test,successors):
    frontier=Stack()
    frontier.push(Node(initial,None))
    explored={initial}
    count=0
    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.state
        count+=1
        if goal_test(current_state):
            return current_node,count
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,current_node))
    return None,count

def bfs(initial,goal_test,successors):
    frontier=Queue()
    frontier.push(Node(initial,None))
    explored={initial}
    count=0
    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.state
        count+=1
        if goal_test(current_state):
            return current_node,count
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,current_node))
    return None,count

def astar(initial, goal_test, successors,heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}
    count=0
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        count+=1
        if goal_test(current_state):
            return current_node,count
        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(initial)))
    return None,count

def node_to_path(node):
    path=[]
    while node.parent is not None:
        node=node.parent
        path.append(node.state)
    path.reverse()
    return path

def main():
    
    pass




if __name__=="__main__":

    main()





