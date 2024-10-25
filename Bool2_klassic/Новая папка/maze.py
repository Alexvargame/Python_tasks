from typing import List,NamedTuple,Callable,Optional
from enum import Enum
import random
from math import sqrt
from generic_search import dfs,bfs,node_to_path,astar,Node
import generic_search1

class Cell(str,Enum):
    EMPTY=' '
    BLOCKED='X'
    START='S'
    GOAL='G'
    PATH='*'

class MazeLocation(NamedTuple):
    row:int
    column:int

class Maze:
    def __init__(self,rows=10,columns=10,sparsness=0.2,start=MazeLocation(0,0),goal=MazeLocation(9,9)):
        self._rows=rows
        self._columns=columns
        self.start=start
        self.goal=goal
        self._grid=[[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows,columns,sparsness)
        self._grid[start.row][start.column]=Cell.START
        self._grid[goal.row][goal.column]=Cell.GOAL

    def _randomly_fill(self,rows,columns,sparsness):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0,1.0)<sparsness:
                    self._grid[row][column]=Cell.BLOCKED

    def __str__(self):
        output=''
        for row in self._grid:
            output+=''.join([c.value for c in row])+'\n'
        return output

    def goal_test(self,ml):
        return ml==self.goal

    def successors(self,ml):
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


def euclidean_distance(goal):
    def distance(ml):
        xdist=ml.column-goal.column
        ydist=ml.row-goal.row
        return sqrt((xdist*xdist)-(ydist*ydist))
    return distance

def manhattan_distance(goal):
    def distance(ml):
        xdist=abs(ml.column-goal.column)
        ydist=abs(ml.row-goal.row)
        return (xdist+ydist)
    return distance

def main():
    M=Maze()
    print(M)
    solution1=dfs(M.start,M.goal_test,M.successors)
    if solution1 is None:
        print('No solutions found')
    else:
        path1=node_to_path(solution1)
        M.mark(path1)
        print('dfs',M)
        M.clear(path1)
    print()
    solution2 = bfs(M.start, M.goal_test, M.successors)
    if solution2 is None:
        print('No solutions found')
    else:
        path2 = node_to_path(solution2)
        M.mark(path2)
        print('bfs',M)
        M.clear(path2)
    distance=manhattan_distance(M.goal)
    solution3 = astar(M.start, M.goal_test, M.successors,distance)
    if solution3 is None:
        print('No solutions found')
    else:
        path3 = node_to_path(solution3)
        M.mark(path3)
        print('astar', M)
        M.clear(path3)
    count_dfs=[]
    count_bfs=[]
    count_astar=[]
    for i in range(100):
        M = Maze()
        sol = generic_search1.dfs(M.start, M.goal_test, M.successors)
        if sol[0] is None:
            continue
            #print('No solutions found')
        else:
            path1 = node_to_path(sol[0])
            M.mark(path1)
            M.clear(path1)
        count_dfs.append(sol[1])
        sol1 = generic_search1.bfs(M.start, M.goal_test, M.successors)
        if sol1[0] is None:
            continue
            # print('No solutions found')
        else:
            path1 = node_to_path(sol1[0])
            M.mark(path1)
            M.clear(path1)
        count_bfs.append(sol1[1])
        distance = manhattan_distance(M.goal)
        sol2= generic_search1.astar(M.start, M.goal_test, M.successors,distance)
        if sol2[0] is None:
            continue
            # print('No solutions found')
        else:
            path1 = node_to_path(sol2[0])
            M.mark(path1)
            M.clear(path1)
        count_astar.append(sol2[1])

    print('DFS','min', min(count_dfs),'max',max(count_dfs),'avg',sum(count_dfs)/len(count_dfs))
    print('BFS','min', min(count_bfs),'max',max(count_bfs),'avg',sum(count_bfs)/len(count_bfs))
    print('ASTAR','min', min(count_astar),'max',max(count_astar),'avg',sum(count_astar)/len(count_astar))






if __name__=="__main__":
    main()





