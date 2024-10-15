from __future__ import annotations
from heapq import heappop,heappush
from collections import namedtuple
from math import sqrt


State = namedtuple('State','y x')

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
    def __init__(self,state,passable,parent=None,cost=0.0,heuristic=0.0):
        self.state=state
        self.passable=passable
        self.parent=parent
        self.heuristic = heuristic
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.heuristic) > (other.cost + other.heuristic)


def astar(initial, goal_test, successors, heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial, True,None, 0.0, heuristic(initial)))
    explored = {initial: 0.0}
    while not frontier.empty:

        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print(explored[current_node.state])
            return current_node
        for child in successors(current_state):
            xdist = child.x - current_state.x
            ydist = child.y - current_state.y
            print('DISTANCE',sqrt((xdist * xdist) + (ydist * ydist)))
            print("HEURCHILD",child,heuristic(child))
            new_cost = current_node.cost + sqrt((xdist * xdist) + (ydist * ydist))#heuristic(child)
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, True,current_node, new_cost, heuristic(child)))
    return None
def euclidean_distance(goal):
    def distance(ml):
        xdist = ml.x - goal.x
        ydist = ml.y - goal.y
        #print('DIS',sqrt((xdist * xdist) + (ydist * ydist)))
        return sqrt((xdist * xdist) + (ydist * ydist))
    return distance
def node_to_path(node):
    path=[node.state]
    while node.parent is not None:
        node=node.parent
        path.append(node.state)
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
        for row in list(zip(*self._grid)):
            output+=''.join([str(c) for c in row])+'\n'
        return output

    def goal_test(self,ml):
        return ml==self.goal

    def successors(self,ml):
        locations=[]
        if ml.y+1<self._rows and self._grid[ml.y+1][ml.x].passable:#!='X':
            locations.append(State(ml.y+1,ml.x))
        if ml.y-1>=0 and self._grid[ml.y-1][ml.x].passable:#!='X':
            locations.append(State(ml.y-1,ml.x))
        if ml.x+1<self._columns and self._grid[ml.y][ml.x+1].passable:#!='X':
            locations.append(State(ml.y,ml.x+1))
        if ml.x-1>=0 and self._grid[ml.y][ml.x-1].passable:#!='X':
            locations.append(State(ml.y,ml.x-1))
        if ml.y+1<self._rows and ml.x+1<self._columns and self._grid[ml.y+1][ml.x+1].passable:#!='X':
            locations.append(State(ml.y+1,ml.x+1))
        if ml.y-1>=0 and ml.x+1<self._columns and self._grid[ml.y-1][ml.x+1].passable:#!='X':
            locations.append(State(ml.y-1,ml.x+1))
        if ml.y+1<self._rows and ml.x-1>=0 and self._grid[ml.y+1][ml.x-1].passable:#!='X':
            locations.append(State(ml.y+1,ml.x-1))
        if ml.y-1>=0 and ml.x-1>=0 and self._grid[ml.y-1][ml.x-1].passable:#!='X':
            locations.append(State(ml.y-1,ml.x-1))
        if ml.x==41 and ml.y==17:
            print(self._grid[ml.y+1][ml.x+1]!='X')
            print(locations)
            input()
        return locations

    def mark(self,path):
        for maze_location in path:

            self._grid[maze_location.y][maze_location.x]='P'
        self._grid[self.start.y][self.start.x]='S'
        self._grid[self.goal.y][self.goal.x]='G'
        for ml in self._grid:
            for mll in ml:
                if mll not in ['P','S','G','X','.']:
                    if self._grid[mll.state.y][mll.state.x].passable:
                        self._grid[mll.state.y][mll.state.x] = '.'
                    else:
                        self._grid[mll.state.y][mll.state.x] = 'X'


    def clear(self,path):
        for maze_location in path:
            self._grid[maze_location.x][maze_location.y] = '.'
        self._grid[self.start.x][self.start.y] = 'S'
        self._grid[self.goal.x][self.goal.y] = 'G'


def wire_DHD_SG1(grid_blueprint):
    #print('NA',grid_blueprint)
    grid, start_node, end_node = make_grid(grid_blueprint)
    print(start_node,end_node)
    M=Maze(grid, start_node, end_node)
    point_distance=euclidean_distance(M.goal)
    solution = astar(M.start, M.goal_test, M.successors,point_distance)
    if solution is None:
       return f'Oh for crying out loud...'
    else:
        print('Solution',solution)
        path = node_to_path(solution)
        # for p in path:
        #     print(p)
        M.mark(path)
        print('Mark_path\n',M)
        M.clear(path)

def make_grid(grid_blueprint):
    """Convert a list of lists of 0's and 1's to a graph of Node objects"""
    grid_blueprint=grid_blueprint.strip()
    width=len(grid_blueprint.split('\n'))
    height=len(grid_blueprint.split('\n')[0])
    print(width,height)
    grid_blueprint = grid_blueprint.replace('\n', '')
    grid = []
    start_node, end_node = None, None
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = grid_blueprint[y * height +x]
            node = Node(state=State(x, y), passable=False if char=='X' else True)
            if char == 'S':
                start_node = node
            elif char == 'G':
                end_node = node
            grid[x].append(node)
    return grid, start_node.state, end_node.state

def main():
    grid_blueprint = """
X.XXXXXX..X.XXXX.X...X.X...XXXXX.X..X...XX..XX
.XXX....X....X.X....XX.XX...X.XX...X.XXXXXX..X
.XXX...X.XXXXXX.XXXX.....X.XX...XXXXX.X....X..
X.XXXX..X.XX..X.X.XXXX.XXXX.XX..X.XXX.XXXXXXXX
.....XX.XX.X.XXXX..XX.X.....X.X....XXX.X..XX..
X..XXXX.XXXXXXXX..XX.X.XX.XXXXXXX..X....XXXX.X
X.X.X..XXXX...XXXXX...XX.XX.XX.XX.XXXXXXX....X
XX..X..XXX.XXX.X.XX..XX.XX..X..X.X..XXX..XXXXX
XX.X..XX.X...XXXX.XX..XXXX.X....XXXX...XXXX...
.XXX.X.X.X.XXXX.X.X.X....X...X..XX.X..........
XXXXXXXX.XXXX.XX....XXX..XXXXX...XXX.XXX....XX
..XX.X..XX.XXXXXX..XX..XX.XX.X..XXXXXX.XX.XX.X
XX..XX.X..X.XXXX..XXX.XX.....X.X.X.X..XX.XXXXX
X.X.XX.XXXX.XX.XXXXX.XXXXXX..X.X...XX.XXXX..XX
X...XX.X.X.X.XXX..XXXX.....XXX..XX..X.XXXXX.X.
.XXX...XXX.XX..X.XXX.XXX.XX.....XXX......XX..X
X.XXXXX...XXXXXXX..XXXX.XXX.XXXXXXXXX.XXXXXX..
...X.XX...G.X..XXX..X.XX...XXXX.XXX.X.XX..X.XX
.XX.XX.X.SX..X.XXX.X..X..XXXXX...X..X.XXXX.X..
.X..XXX.XXXX.X.......X....XXX..XX.X..XX..XXX..
"""

    print(wire_DHD_SG1(grid_blueprint))


    
    
  
    
if __name__ == "__main__":
    main()
