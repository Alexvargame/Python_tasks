from __future__ import annotations

from heapq import heappop,heappush
from collections import namedtuple

class PriorityQueue():
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

class Node():
    def __init__(self,state,parent,cost=0.0,heuristic=0.0):
        self.state=state
        self.parent=parent
        self.cost=cost
        self.heuristic=heuristic
    def __lt__(self,other):
        return (self.cost+self.heuristic)<(other.cost+other.heuristic)


def astar(initial,goal_test, successors,heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}
    while not frontier.empty:
        
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost = current_node.cost + heuristic(child)
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(initial)))
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
        if ml[0]+1<self._rows:
            locations.append(MazeLocation(ml[0]+1,ml[1]))
        if ml[0]-1>=0:
            locations.append(MazeLocation(ml[0]-1,ml[1]))
        if ml[1]+1<self._columns:
            locations.append(MazeLocation(ml[0],ml[1]+1))
        if ml[1]-1>=0:
            locations.append(MazeLocation(ml[0],ml[1]-1))
        return locations
        
    def res(self,path):
        res=[]
        for maze_location in path:
            if maze_location[0]<path[path.index(maze_location)-1][0]:
                res.append('up')
            elif maze_location[0]>path[path.index(maze_location)-1][0]:
                res.append('down')
            elif maze_location[1]<path[path.index(maze_location)-1][1]:
                res.append('left')           
            else:
                res.append('right')
        return res[1:]
            



    
def set_points(M):
    def point(ml):
        return M._grid[ml[0]][ml[1]]
    return point
    
def cheapest_path(t, start, finish):
    print(t, start, finish)
    M=Maze(t, start, finish)
    distance=set_points(M)    
    solution = astar(M.start,M.goal_test, M.successors,distance)
    if solution is None:
        print('No solutions found')
    else:
        path=node_to_path(solution)
    return M.res(path)
    
def main():

    print(cheapest_path([[1,9,1],[2,9,1],[2,1,1]], (0,0), (0,2)))

    
    
  
    
if __name__ == "__main__":
    main()
