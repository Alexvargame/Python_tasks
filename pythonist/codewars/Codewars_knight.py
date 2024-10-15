from __future__ import annotations

from heapq import heappop,heappush
from collections import namedtuple,deque

class Queue():
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

class Node():
    def __init__(self,state,parent,cost=0.0,heuristic=0.0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic
    def __lt__(self,other):
        return (self.cost+self.heuristic)<(other.cost+other.heuristic)


def bfs(initial, goal_test, successors):
    print('BFS', initial)
    frontier = Queue()
    frontier.push(Node(initial, None))
    explored = {initial}

    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None

def node_to_path(node):
    path=[node.state]
    while node.parent is not None:
        node=node.parent
        path.append(node.state)
    path.reverse()
    return path

MazeLocation=namedtuple('MazeLocation','row column')
class Maze:
    def __init__(self,t,start,finish):
        self._rows=len(t)
        self._columns=len(t[0])
        self.start=start
        self.goal=finish
        self._grid=t

    def __str__(self):
        output=''
        for row in self._grid:
            output+=''.join([str(c) for c in row])+'\n'
        return output

    def goal_test(self,ml):
        return ml==self.goal

    def successors(self,ml):
        locations=[]
        if ml[0]-1>=0 and ml[1]-2>=0:
            locations.append(MazeLocation(ml[0]-1,ml[1]-2))
        if ml[0]-2>=0 and ml[1]-1>=0:
            locations.append(MazeLocation(ml[0]-2,ml[1]-1))
        if ml[0]+1<=self._rows and ml[1]-2>=0:
            locations.append(MazeLocation(ml[0]+1,ml[1]-2))
        if ml[0]+2<=self._rows and ml[1]-1>=0:
            locations.append(MazeLocation(ml[0]+2,ml[1]-1))
        if ml[0]-1>=0 and ml[1]+2<=self._columns:
            locations.append(MazeLocation(ml[0]-1,ml[1]+2))
        if ml[0]-2>=0 and ml[1]+1<=self._columns:
            locations.append(MazeLocation(ml[0]-2,ml[1]+1))
        if ml[0]+1<=self._rows and ml[1]+2<=self._columns:
            locations.append(MazeLocation(ml[0]+1,ml[1]+2))
        if ml[0]+2<=self._rows and ml[1]+1<=self._columns:
            locations.append(MazeLocation(ml[0]+2,ml[1]+1))
        if ml[0]==5 and ml[1]==6:
            print('ML',ml,'loc',locations)

        return locations

def knight(p1, p2):
    desk_dict={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    desk=[['*' for i in range(1,9)] for j in range(1,9)]
    start=(desk_dict[p1[0]],int(p1[1]))
    finish=(desk_dict[p2[0]],int(p2[1]))
    print('POINTS',start, finish)
    M=Maze(desk, start, finish)
    print(M.start[0])
    solution = bfs(M.start,M.goal_test, M.successors)
    if solution is None:
        print('No solutions found')
    else:
        path=node_to_path(solution)
        print('PATH',path)
    return len(path)-1
    
def main():

    print(knight('b3', 'd8'))

    
    
  
    
if __name__ == "__main__":
    main()
