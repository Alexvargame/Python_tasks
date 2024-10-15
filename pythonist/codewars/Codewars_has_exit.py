from __future__ import annotations
from heapq import heappop,heappush
from collections import namedtuple
from collections import deque

Position=namedtuple('Position','y x')

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
    def __init__(self,position,passable):
        self.position=position
        self.passable=passable



def bfs(initial,goal_test,successors):
    print('BFS',initial.position.x,initial.position.y)
    frontier=Queue()
    frontier.push(Node(initial.position,True))
    explored={initial}
    
    while not frontier.empty:
        #print('EX',explored)
        current_node=frontier.pop()
        current_state=current_node.position
        # print(current_state,current_node,current_node.position)
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,True))
    return None

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
        # print('mp_g',ml)
        # print('gaol',self.goal)
        return ml==self.goal.position

    def successors(self,ml):
        locations=[]
        if ml.y+1<self._rows and self._grid[ml.y+1][ml.x].passable:
            locations.append(Position(ml.y+1,ml.x))
        if ml.y-1>=0 and self._grid[ml.y-1][ml.x].passable:
            locations.append(Position(ml.y-1,ml.x))
        if ml.x+1<self._columns and self._grid[ml.y][ml.x+1].passable:
            locations.append(Position(ml.y,ml.x+1))
        if ml.x-1>=0 and self._grid[ml.y][ml.x-1].passable:
            locations.append(Position(ml.y,ml.x-1))
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



def has_exit(maze):
    grid, start_node, end_node = make_maze(maze)
    print(start_node.position,[(e.position.x,e.position.y) for e in end_node])
    for goal in end_node:
        M = Maze(grid, start_node, goal)
        solution = bfs(M.start, M.goal_test, M.successors)
        if solution:
            return True

    return False
def make_maze(maze):
    grid = []
    for i in maze:
        print(i,sep='\n')

    len_max=max([len(i) for i in maze])
    maze = [m+' '*(len_max-len(m)) for m in maze]
    print([len(i) for i in maze])
    start_node, end_node = None, []
    for x in range(0, len(maze)):
        grid.append([])
        for y in range(0, len(maze[0])):
            #print('x',x,'y',y,'maze',maze[x][y])
            char = maze[x][y]
            node = Node(position=Position(x, y), passable=False if char == '#' else True)
            if char == 'k':
                start_node = node
            elif char == ' ' and (x in [0,len(maze)-1] or y in [0,len(maze[0])-1]):
                end_node.append(node)
            grid[x].append(node)

    return grid, start_node, end_node
def main():
    maze = [' #   #####', '##     ## ', '#    #####', '     # # #', ' ## # # ##', '#### k### ', '  ### # ##', '# # ### ##', '  ##    ##', '  # # #   ']
    print([len(i) for i in maze])

    print(has_exit(maze))


    
    
  
    
if __name__ == "__main__":
    main()
