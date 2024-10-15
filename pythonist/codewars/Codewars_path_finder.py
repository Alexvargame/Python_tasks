from __future__ import annotations
from enum import Enum
from heapq import heappop,heappush
from collections import namedtuple
from collections import deque

class Cell(str,Enum):
    EMPTY='.'
    BLOCKED='W'
    START='S'
    GOAL='G'
    PATH='*'

MazeLocation=namedtuple('MazeLcation','row column')

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
    def __init__(self,position,passable=None):
        self.position=position
        self.passable=passable



def bfs(initial,goal_test,successors):
    print('BFS',initial)
    frontier=Queue()
    frontier.push(Node(initial.position,True))
    explored={initial}
    
    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.position
        if goal_test(current_state):
            print('CST',current_state,current_node)
            return True
            #return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,True))
    return False#None

def node_to_path(node):
    path=[node.position]
    while node.parent is not None:
        node=node.parent
        path.append(node.position)
    path.reverse()
    return path

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
        return ml==self.goal.position

    def successors(self, ml):
        locations = []

        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != 'W':
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] !='W':
            locations.append(MazeLocation(ml.row - 1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != 'W':
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] !='W':
            locations.append(MazeLocation(ml.row, ml.column - 1))
        print(ml,self._grid[ml.column][ml.row],locations)
        return locations

    def mark(self,path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column]=Cell.PATH
        self._grid[self.start.row][self.start.column]=Cell.START
        self._grid[self.goal.row][self.goal.column]=Cell.GOAL

    def clear(self,path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL



def path_finder(maze):
    start_node = Node(position=MazeLocation(0, 0))
    end_node = Node(position=MazeLocation(len(maze[0])-1 , len(maze[0])-1 ))
    M=Maze(maze, start_node, end_node)
    print('MGRID',M._grid,M._rows,M._columns)
    solution = bfs(M.start, M.goal_test, M.successors)
    return solution
    # if solution is None:
    #     print('No solutions found')
    # else:
    #     print('S',solution)

def main():

    maze=[
  '....',
  '.W..',
  'W.WW',
  '.W..',
]

    print(path_finder(maze))

    
    
  
    
if __name__ == "__main__":
    main()
