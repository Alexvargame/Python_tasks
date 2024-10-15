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


class Peak():
    def __init__(self,position,peak,char,dry):
        self.position=position
        self.peak=peak
        self.char=char
        self.dry=dry





class Plato:
    def __init__(self,t):
        self._rows=len(t)
        self._columns=len(t[0])
        self._grid=t

    def __str__(self):
        output=''
        for row in self._grid:
            output+=''.join([str(c) for c in row])+'\n'
        return output

    def successors(self,ml):
        locations=[]
        if ml.x+1<self._rows and self._grid[ml.x+1][ml.y].peak!=-0.5:
            locations.append(Position(ml.x+1,ml.y))
        if ml.x-1>=0 and self._grid[ml.x-1][ml.y].peak!=-0.5:
            locations.append(Position(ml.x-1,ml.y))
        if ml.y+1<self._columns and self._grid[ml.x][ml.y+1].peak!=-0.5:
            locations.append(Position(ml.x,ml.y+1))
        if ml.y-1>=0 and self._grid[ml.x][ml.y-1].peak!=-0.5:
            locations.append(Position(ml.x,ml.y-1))
        return locations

    def successors_river(self,ml):
        locations=[]
        if ml.x+1<self._rows and self._grid[ml.x+1][ml.y].dry=='water':
            locations.append(Position(ml.x+1,ml.y))
        if ml.x-1>=0 and self._grid[ml.x-1][ml.y].dry=='water':
            locations.append(Position(ml.x-1,ml.y))
        if ml.y+1<self._columns and self._grid[ml.x][ml.y+1].dry=='water':
            locations.append(Position(ml.x,ml.y+1))
        if ml.y-1>=0 and self._grid[ml.x][ml.y-1].dry=='water':
            locations.append(Position(ml.x,ml.y-1))
        return locations

    def mark(self,path):
        for i in range(self._rows):
            for j in range(self._columns):
                if self._grid[i][j].position in path:
                    self._grid[i][j]='#'
                else:
                    if self._grid[i][j].passable:
                        self._grid[i][j]='0'
                    else:
                        self._grid[i][j]='1'

        # for maze_location in path:
        #     self._grid[maze_location.x][maze_location.y]='#'
        # if maze_location not in path:
        #     self._grid[maze_location.x][maze_location.y]='1'
        self._grid[self.start.position.x][self.start.position.y]='S'
        self._grid[self.goal.position.x][self.goal.position.y]='E'

    def clear(self,path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY

        self._grid[self.start.row][self.start.column] = 'S'
        self._grid[self.goal.row][self.goal.column] = 'E'


def around_peak(peak,P,p):
    #print(peak.position, peak.peak)
    frontier = Queue()
    initial = peak
    frontier.push(Peak(initial.position, initial.peak, initial.char,initial.dry))
    explored = {initial}
    while not frontier.empty:
        current_peak = frontier.pop()
        current_state = current_peak.position
        # print(p,current_state,P.successors(current_state),[P._grid[s.x][s.y].peak for s in P.successors(current_state) if P._grid[s.x][s.y].peak==peak.peak])
        # input()
        if P.successors_river(current_state):
            return 0
        for child in P.successors(current_state):
            if P._grid[child.x][child.y].peak==peak.peak:
                # print('child',child)
                if child in explored:
                    continue
                explored.add(child)
                frontier.push(Peak(child, P._grid[child.x][child.y].peak,P._grid[child.x][child.y].char,P._grid[child.x][child.y].dry))
    return 1
def print_peak_height(grid):

    output = ''
    for row in grid:
        output += ''.join([str(c.peak) if type(c.peak)==int else '-' for c in row]) + '\n'
    return output
def print_peak_height_1(grid,p):
    output = ''
    for row in grid:
        output += ''.join([str(c.peak) if c.peak>p-0.5 else '-' for c in row]) + '\n'
    return output
def print_dry(grid):
    output = ''
    for row in grid:
        output += ''.join([c.dry[0] for c in row]) + '\n'
    return output

def count_dry(grid):
    drys=0
    for row in grid:
        #print(row)
        drys+=sum([1 if p.dry=='dry' else 0 for p in row])
    return drys
def dry_ground(grid):
    # if not grid:
    #     return (0,0,0,0)
    # if not any(['-' in gr for gr in grid]):
    #     return (len(grid) * len(grid[0]), len(grid) * len(grid[0]), len(grid) * len(grid[0]),
    #             len(grid) * len(grid[0]))
    dry_lst=[]
    P = Plato(grid)
    for p in range(4):
        print('DRY', count_dry(P._grid))
        # dry=0
        # not_dry = 0
        double_check=[]
        dry_lst.append(count_dry(P._grid))
        for i in range(P._rows):
            for j in range(P._columns):
                # if P._grid[i][j].dry =='dry':
                #     dry += 1
                if P._grid[i][j].peak>p:
                    if len(P.successors(P._grid[i][j].position))==4:
                        min_peak=min([P._grid[s.x][s.y].peak for s in P.successors(P._grid[i][j].position)])
                        P._grid[i][j].peak=min_peak+1
                else:
                    double_check.append(P._grid[i][j])
                    if not around_peak(P._grid[i][j], P, p):
                        P._grid[i][j].dry='water'
        print('DRY_1', count_dry(P._grid))
        # print(print_peak_height_1(grid, p))
        print(print_dry(grid))

        if p > 0:
            for pp in double_check:
                if not around_peak(pp, P, p):
                    # if pp.dry=='dry':
                    #     not_dry+=1
                    pp.dry = 'water'

        #dry-not_dry)
        print(dry_lst)
        print(print_peak_height(grid))
        print(print_peak_height_1(grid,p))
        print(print_dry(grid))



def make_grid(terrain):
    peak_dict={'^':1, ' ': 0, '-':-0.5}
    grid = []
    width=len(terrain[0])
    height=len(terrain)
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = terrain[x][y]
            node = Peak(position=Position(x, y), peak=peak_dict[char],char=char,dry='dry' if char!='-' else 'water')
            grid[x].append(node)
    return grid

def main():
    # terrain = (
    #         "  ^^^^^^             ",
    #         "^^^^^^^^       ^^^   ",
    #         "^^^^^^^  ^^^         ",
    #         "^^^^^^^  ^^^         ",
    #         "^^^^^^^  ^^^         ",
    #         "---------------------",
    #         "^^^^^                ",
    #         "   ^^^^^^^^  ^^^^^^^ ",
    #         "^^^^^^^^     ^     ^ ",
    #         "^^^^^        ^^^^^^^ ",
    #     )
#     terrain = (
# '                         ',
# '                         ',
# '-------------------------',
# '       ^^^^^^^^^^^^^^^^^^',
# '       ^^^^^^^^^^^^^^^^^^',
# '       ^^^^^^^^^^^^^^^^^^',
# '       ^^^^^        ^^^^^',
# '       ^^^^^        ^^^^^',
# '       ^^^^^^^^^^^^^^^^^^',
# '       ^^^^^^^^^^^^^^^^^^',
# '       ^^^^^^^^^^^^^^^^^^',
#     )
    terrain = (

'     ^^   ^^^^^^^   ',
'--------------------',
'     ^^^^^^^^^^^^   ',
'^^^^^^^^^^^^^^^^^   ',
'^^^^^^^^^^^^^^^^^^^^',
'^^   ^^^^^^^^^ ^^^^^',
'^^   ^^^^^^^^^ ^^^^^',
'^^^^^^^^^   ^^ ^^^^^',
'^^^^^^^^^   ^^^^^^^^',
'^^   ^^^^   ^^^^^   ',
'^^   ^^^^^^^^^      ',
    )

#     terrain = (
# '   ^^^^^^^^^^^^^^^^^',
# '   ^^^^^^^^^^^^^^^^^',
# '   ^^^^^^^^^^ ^^^^^^',
# '    ^^^^^^^   ^^^^^^',
# ' ^^^^^   ^^  ^^^^^^^',
# ' ^^^^^   ^^  ^^^^^^^',
# ' ^^^^^   ^^  ^^^^^  ',
# '    ^^^^^^^     ^^^^',
# '    ^^^^^^^     ^^^^',
# '   ^^^^^        ^^^^',
# '--------------------',
# )
    grid=make_grid(terrain)
    print('eEE',make_grid(terrain))
    print(dry_ground(grid))

    
    
  
    
if __name__ == "__main__":
    main()
