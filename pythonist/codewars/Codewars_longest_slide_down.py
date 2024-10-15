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
        return (self.cost+self.heuristic)>(other.cost+other.heuristic)


    
    
def astar(initial,goal_test, successors,heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored = {initial: heuristic(initial)}
    while not frontier.empty:
       # print('fromt',frontier)
        current_node = frontier.pop()
        current_state = current_node.state
      #  print('befor',explored)
       # print('CCC',current_node,current_node.cost,current_state)
        if goal_test(current_state):
            #print('GOAL')
            return current_node
        for child in successors(current_state):
            new_cost = current_node.cost + heuristic(child)
           # print('CHILD',child,new_cost,heuristic(child))
##            if explored[child]:
##                print('exp',child,explored[child])
           # input()                  
            if child not in explored or explored[child] < new_cost:
                explored[child] = new_cost
              #  print('after',explored)
               # print('node',Node(child, current_node, new_cost, heuristic(child)))
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
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
           # print('ch',(ml[0]+1,ml[1]),(ml[0]+1,ml[1]+1))
            locations.append(MazeLocation(ml[0]+1,ml[1]))
            locations.append(MazeLocation(ml[0]+1,ml[1]+1))
##        if ml[0]-1>=0:
##            locations.append(MazeLocation(ml[0]-1,ml[1]))
##        if ml[1]+1<self._columns:
##            locations.append(MazeLocation(ml[0],ml[1]+1))
##        if ml[1]-1>=0:
##            locations.append(MazeLocation(ml[0],ml[1]-1))
        #print('local',ml,locations)
        return locations
        
    def res(self,path):
        res=0
        for maze_location in path:
            #print(maze_location,self._grid[maze_location[0]][maze_location[1]])
            res+=self._grid[maze_location[0]][maze_location[1]]
##            if maze_location[0]<path[path.index(maze_location)-1][0]:
##                res.append('up')
##            elif maze_location[0]>path[path.index(maze_location)-1][0]:
##                res.append('down')
##            elif maze_location[1]<path[path.index(maze_location)-1][1]:
##                res.append('left')           
##            else:
##                res.append('right')
        return res
            



    
def set_points(M):
    def point(ml):
        return M._grid[ml[0]][ml[1]]
    return point
    


def longest_slide_down(pyramid):
    res=[]
    print(pyramid)
    
    for i in range(len(pyramid[-1])):
        print('END',(len(pyramid)-1,i))
        M=Maze(pyramid, (0,0), (len(pyramid)-1,i))
        distance=set_points(M)
        solution = astar(M.start,M.goal_test, M.successors,distance)
        if solution is None:
            print('No solutions found')
        else:
            path=node_to_path(solution)
        print('path',path)
        print('p',M.res(path))
        input()
        res.append(M.res(path))
    return max(res)
def main():
    print(longest_slide_down([
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20,  4, 82, 47, 65],
            [19,  1, 23, 75,  3, 34],
            [88,  2, 77, 73,  7, 63, 67],
            [99, 65,  4, 28,  6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
            ]))
   # print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))
    
  
    
if __name__ == "__main__":
    main()
