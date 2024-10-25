from enum import Enum
from typing import NamedTuple, List, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, node_to_path, Node,bfs,astar


class Cell(str, Enum):
    EMPTY=''
    BLOCKED='X'
    START='S'
    GOAL='G'
    PATH='*'

class MazeLocation(NamedTuple):
    #self.row=row
    row:int
    #self.column=column
    column:int

class Maze:
    def __init__(self, rows=10,columns=10, spareness=0.2, start=MazeLocation(0,0),goal=MazeLocation(9,9)):
        self._rows=rows
        self._columns=columns
        self.start=start
        self.goal=goal
        self._grid=[[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, spareness)
        self._grid[start.row][start.column]=Cell.START
        self._grid[goal.row][goal.column]=Cell.GOAL

    def _randomly_fill(self, rows, columns,spareness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0,1.0)<spareness:
                    self._grid[row][column]=Cell.BLOCKED
                    
    

    def __str__(self):
        output=' '
        for row in self._grid:
            output+=''.join([c.value for c in row])+'\n'
        return output
    def goal_test(self, ml):
        return ml==self.goal


    def successors(self, ml):
        locations=[]
        if ml.row+1<self._rows and self._grid[ml.row+1][ml.column]!=Cell.BLOCKED:
            locations.append(MazeLocation(ml.row+1,ml.column))
        if ml.row-1>=0 and self._grid[ml.row-1][ml.column]!=Cell.BLOCKED:
            locations.append(MazeLocation(ml.row-1,ml.column))
        if ml.column+1<self._columns and self._grid[ml.row][ml.column+1]!=Cell.BLOCKED:
            locations.append(MazeLocation(ml.row,ml.column+1))
        if ml.column-1>=0 and self._grid[ml.row][ml.column-1]!=Cell.BLOCKED:
            locations.append(MazeLocation(ml.row,ml.column-1))
        return locations
    def mark(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column]=Cell.PATH
        self._grid[self.start.row][self.start.column]=Cell.START
        self._grid[self.goal.row][self.goal.column]=Cell.GOAL

    def clear(self, path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column]=Cell.EMPTY
        self._grid[self.start.row][self.start.column]=Cell.START
        self._grid[self.goal.row][self.goal.column]=Cell.GOAL

def euclidian_distance(goal):
    def distance(ml):
        xdist=ml.column-goal.column
        ydist=ml.row-goal.row
        return sgrt(xdist**2 + ydist**2)
    return distance

def manhattan_distance(goal):
    def distance(ml):
        xdist=abs(ml.column-goal.column)
        ydist=abs(ml.row-goal.row)
        return xdist + ydist
    return distance

if __name__=="__main__":
    m=Maze()
    print("@",m)
    print("----")
    solution1=dfs(m.start, m.goal_test, m.successors)
    if solution1 is None:
        print("No")
    else:
        path1=node_to_path(solution1)
        m.mark(path1)
        print("1",m)
        print("---")
        m.clear(path1)

    solution2=bfs(m.start, m.goal_test, m.successors)

    if solution2 is None:
        print("No")
    else:
        path2=node_to_path(solution2)
        m.mark(path2)
        print("2",m)
        print("---")
        m.clear(path2)

    distance=manhattan_distance(m.goal)
    solution3=astar(m.start, m.goal_test,m.successors, distance)
    if solution3 is None:
        print("No solution found using А*!")
    else:   
        path3=node_to_path(solution3)
        m.mark(path3)
        print("3",m)
        print("---")
        

