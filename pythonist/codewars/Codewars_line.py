from __future__ import annotations
from collections import namedtuple
from collections import deque

Position=namedtuple('Position','x y')

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
    def __init__(self,position,char,parent=None):
        self.position=position
        self.char=char
        self.parent=parent


def way(initial,goal_test,successors,points):
    print('BFS',initial)
    frontier=Queue()
    count=0
    frontier.push(Node(initial.position,initial.char,None))
    explored={initial}
    print([p.position for p in successors(initial.position)])
    while not frontier.empty:
        current_node=frontier.pop()
        count+=1
        current_state=current_node.position
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            # if current_node.parent and current_node.parent.char=='+' and current_node.char=='+':
            #     print('CHAR1', current_node.parent.position, current_node.parent.char, current_node.char)
            #     print(current_node.parent.position,current_node.position,'!',child.position,'POS',current_node.parent.position.x==child.position.x,current_node.parent.position.y==child.position.y)
            #     if child.char=='+' and (current_node.parent.position.x==child.position.x or current_node.parent.position.y==child.position.y):
            #         continue
            frontier.push(Node(child.position,child.char,current_node))
    return None

def node_to_path(node):
    path=[node.position]
    while node.parent is not None:
        node=node.parent
        path.append(node.position)
    path.reverse()
    return path

class Maze:
    def __init__(self,t,start,finish,points):
        self._rows=len(t)
        self._columns=len(t[0])
        self.start=start
        self.goal=finish
        self._grid=t
        self.points=points

    def __str__(self):
        output=''
        for row in self._grid:
            output+=''.join([c.char for c in row])+'\n'
        return output
    def print_mark(self):
        output=''
        for row in self._grid:
            output+=''.join([c for c in row])+'\n'
        return output
    def goal_test(self,ml):
        return ml==self.goal.position

    def successors(self,ml):
        locations=[]
        if self._grid[ml.x][ml.y].char!='-':
            if ml.x+1<self._rows and self._grid[ml.x+1][ml.y].char not in ['-',' '] :
                if self._grid[ml.x+1][ml.y].char != '+':
                    locations.append(self._grid[ml.x+1][ml.y])
                else:
                    if (ml.y + 1 < self._columns and ml.x + 1 < self._rows and self._grid[ml.x + 1][ml.y + 1].char in ['-','+','X']
                            or ml.y + 1 < self._columns and ml.x + 1 < self._rows and self._grid[ml.x + 1][ml.y - 1].char in ['-','+','X'])  :
                        locations.append(self._grid[ml.x+1][ml.y])
            if ml.x-1>=0 and self._grid[ml.x-1][ml.y].char not in ['-',' ']:
                if self._grid[ml.x - 1][ml.y].char != '+':
                    locations.append(self._grid[ml.x - 1][ml.y])
                else:
                    if (ml.y + 1 < self._columns and ml.x - 1 < self._rows and self._grid[ml.x - 1][ml.y + 1].char in ['-','+','X']
                            or ml.y + 1 < self._columns and ml.x - 1 < self._rows and self._grid[ml.x - 1][ml.y - 1].char in ['-', '+','X']):
                        locations.append(self._grid[ml.x - 1][ml.y])
        if self._grid[ml.x][ml.y].char!='|':
            if ml.y+1<self._columns and self._grid[ml.x][ml.y+1].char not in ['|',' ']:
                if self._grid[ml.x][ml.y+1].char!='+':
                    locations.append(self._grid[ml.x][ml.y+1])
                else:
                    if (ml.y+1<self._columns and ml.x+1<self._rows and self._grid[ml.x+1][ml.y+1].char in ['|','+','X']
                            or ml.y+1<self._columns and ml.x-1<self._rows and self._grid[ml.x-1][ml.y+1].char in ['|','+','X']) :
                        locations.append(self._grid[ml.x][ml.y+1])
            if ml.y-1>=0 and self._grid[ml.x][ml.y-1].char not in ['|',' ']:
                if self._grid[ml.x][ml.y - 1].char != '+':
                    locations.append(self._grid[ml.x][ml.y - 1])
                else:
                    if (ml.y - 1 < self._columns and ml.x + 1 < self._rows and self._grid[ml.x + 1][ml.y - 1].char in ['|',  '+','X']
                            or ml.y - 1 < self._columns and ml.x - 1 < self._rows and self._grid[ml.x - 1][ml.y - 1].char in ['|', '+','X']):
                        locations.append(self._grid[ml.x][ml.y - 1])
        #print('LOCCCC',self._grid[ml.x][ml.y].position, [p.position for p in locations])
        return locations

    def mark(self,path):
        for i in range(self._rows):
            for j in range(self._columns):
                if self._grid[i][j].position in path:
                    self._grid[i][j]='#'
                else:
                    self._grid[i][j]='.'


        # for maze_location in path:
        #     self._grid[maze_location.x][maze_location.y]='#'
        # if maze_location not in path:
        #     self._grid[maze_location.x][maze_location.y]='1'
        self._grid[self.start.position.x][self.start.position.y]='X'
        self._grid[self.goal.position.x][self.goal.position.y]='X'
        return self._grid
    # def points_(self,path):
    #     p_count=0
    #     for i in range(self._rows):
    #         for j in range(self._columns):
    #             if self._grid[i][j].char in ['+'] and self._grid[i][j].position not in path:
    #                 p_count+=1
    #     return p_count
def line(grid):
    M=Maze(*make_grid(grid))
    print(M)
    # print(M.start.position)
    # print([p.position for p in M.successors(M.start.position)])
    print('POINTS',M.points)

    solution = way(M.start, M.goal_test, M.successors,M.points)
    print('SOL',solution)
    if solution is None:
        print('No solutions found')
    else:

        path = node_to_path(solution)
        print('PATH',len(path))
        print('+++',M.points_(path))
        if len(path)==M.points:# or len(path)+M.points_(path)==M.points:
            print(True)
        else:
            print(False)

        M.mark(path)
        print(M.print_mark())


def make_grid(grid):
    """Convert a list of lists of 0's and 1's to a graph of Node objects"""
    width=len(grid[0])
    height=len(grid)
    print(width,height)
    grid_res = []
    points = 0
    start_node, end_node = None, None
    for x in range(0, height):
        grid_res.append([])
        for y in range(0, width):
            char = grid[x][y]
            node = Node(position=Position(x, y), char=char)

            if char == 'X' and start_node is None:
                start_node = node
            elif char == 'X' and end_node is None:
                end_node = node
            if char!=' ':
                points+=1
            grid_res[x].append(node)
    return grid_res, start_node, end_node,points

def main():
    # grid = ["                    ",
    #         "     +--------+     ",
    #         "  X--+        +--+  ",
    #         "                 |  ",
    #         "                 X  ",
    # #         "                    "]
    # grid = ["      +------+",
    #         "      |      |",
    #         "X-----+------+",
    #         "      |       ",
    #         "      X       "]
    # grid = [" X  ",
    #         " |  ",
    #         " +  ",
    #         " X  "]
    # grid = ["   |--------+    ",
    #         "X---        ---+ ",
    #         "               | ",
    #         "               X "]
   #grid = ['                      ', '   +-------+          ', '   |      +++---+     ', 'X--+      +-+   X     ']
    # grid = ['   +-----+  ', '   |+---+|  ', '   ||+-+||  ', '   |||X+||  ', '   X|+--+|  ', '    +----+  ']
    #print(make_grid(grid))
    #grid = ['                      ', '   +-------+          ', '   |      +++---+     ', 'X--+      +-+   X     ']
    grid = ['            ', '   X+++     ', '    +++X    ']
    line(grid)
    # grid, start_node, end_node=make_grid(gri    d1_blueprint,5,5)
    # print('eEE',make_grid(grid1_blueprint,5,5))
    # print(find_shortest_path(grid, start_node, end_node))
    # pass # print(cheapest_path([[1,9,1],[2,9,1],[2,1,1]], (0,0), (0,2)))
    #
    #



if __name__ == "__main__":
    main()
