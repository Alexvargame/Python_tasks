from __future__ import annotations
from collections import namedtuple
from math import sqrt
from collections import deque

State=namedtuple('State','y x')

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
    def __init__(self,state,passable,char=None,parent=None):
        self.state=state
        self.passable=passable
        self.char = char
        self.parent=parent



def bfs(initial, goal_test, successors,char):
    print('BFS', initial)

    frontier = Queue()
    frontier.push(Node(initial,True,char))
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
            frontier.push(Node(child,True,'.',current_node))
    return None

def node_to_path(node):
    path=[node.state]
    while node.parent is not None:
        print()
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
        if ml.x==0 and ml.y==0:
            print(self._grid[ml.y+1][ml.x+1]!='X')
            print(locations)
            input()
        return locations

    def mark(self,path):
        for maze_location in path:
            self._grid[maze_location.y][maze_location.x]='P'
        self._grid[self.start.y][self.start.x]='S'
        self._grid[self.goal.y][self.goal.x]='G'
        # for ml in self._grid:
        #     for mll in ml:
        #         if mll not in ['P','S','G','X','.']:
        #             if self._grid[mll.state.y][mll.state.x].passable:
        #                 self._grid[mll.state.y][mll.state.x] = '.'
        #             else:
        #                 self._grid[mll.state.y][mll.state.x] = 'X'
    def res(self,path):
        res_dict= {'>':'RIGHT', '<':'LEFT', '^':'UP', 'v':'DOWN'}
        res=[]
        st_char=self._grid[self.start.y][self.start.x].char
        for maze_location in path[1:]:
            print('SCHAR', st_char)
            print(maze_location,path[path.index(maze_location)-1])
            if maze_location[1]<path[path.index(maze_location)-1][1]:

                if res_dict[st_char]=='UP':
                    res.append('F')
                else:
                    if res_dict[st_char]=='DOWN':
                        res.append('B')
                        res.append('F')
                    elif res_dict[st_char]=='RIGHT':
                        res.append('L')
                        res.append('F')
                    else:
                        res.append('R')
                        res.append('F')
                st_char = '^'
                print(res)
                input()
            elif maze_location[1]>path[path.index(maze_location)-1][1]:
                print('DDDDDDDDDDDD',st_char)
                if res_dict[st_char] == 'DOWN':
                    res.append('F')
                else:
                    if res_dict[st_char] == 'UP':
                        res.append('B')
                        res.append('F')
                    elif res_dict[st_char] == 'LEFT':
                        res.append('L')
                        res.append('F')
                    else:
                        res.append('R')
                        res.append('F')
                st_char = 'v'
                print(res)
                input()
            elif maze_location[0]<path[path.index(maze_location)-1][0]:
                if res_dict[st_char] == 'LEFT':
                    res.append('F')
                else:
                    if res_dict[st_char] == 'UP':
                        res.append('L')
                        res.append('F')

                    elif res_dict[st_char] == 'DOWN':
                        res.append('R')
                        res.append('F')

                    else:
                        res.append('B')
                        res.append('F')
                st_char = '<'
                print(res)
                input()
            else:
                print("RIGHT")

                if res_dict[st_char] == 'RIGHT':
                    res.append('F')
                else:
                    if res_dict[st_char] == 'UP':
                        res.append('R')
                        res.append('F')
                    elif res_dict[st_char] == 'DOWN':
                        res.append('L')
                        res.append('F')
                    else:
                        res.append('B')
                        res.append('F')
                st_char = '>'
                print(res)
                input()
        return res


def escape(grid_blueprint):
    grid, start_node, end_node = make_grid(grid_blueprint)
    M=Maze(grid, start_node.state, end_node[0].state)
    solution = bfs(M.start, M.goal_test, M.successors,start_node.char)
    if solution is None:
       return f'Oh for crying out loud...'
    else:
        path = node_to_path(solution)
        # M.mark(path)
        # print('Mark_path\n',M)
        # # M.clear(path)
        print('path',[p for p in path])
        return M.res(path)

def make_grid(grid_blueprint):
    width=len(grid_blueprint)
    height=len(grid_blueprint[0])
    grid = []
    start_node, end_node = None, []
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = grid_blueprint[y][x]
            if x==0 or x==height-1 or y==0 or y==width-1:
                if char!='#':
                    node = Node(state=State(x, y), passable=True)
                    end_node.append(node)
                else:
                    node = Node(state=State(x, y), passable=False if char=='#' else True,char=char)
            else:
                node = Node(state=State(x, y), passable=False if char == '#' else True,char=char)
            if char in  ['>','<','^','v']:
                start_node = node
            grid[x].append(node)
    return grid, start_node,end_node

def main():
    grid_blueprint = ['###',
                      '  #',
                      '# #',
                      '# #',
                      '# #',
                      '# #',
                      '# #',
                      '# #',
                      '# #',
                      '#>#',
                      '###']


    print(escape(grid_blueprint))


    
    
  
    
if __name__ == "__main__":
    main()
