from __future__ import annotations
from collections import namedtuple

State=namedtuple('State','x y')


class Figure():
    def __init__(self,state,parent=None,char='',cost=''):
        self.state=state
        self.parent=parent
        self.char=char
        self.cost=cost


def checks(king, goal_test, successors, grid,figures):
    print(king.state)
    for f in figures:
        if goal_test(f):
            return True
    return False




class Maze:
    def __init__(self,t,king,figures=[]):
        self._rows=len(t)
        self._columns=len(t[0])
        self.king=king
        self._grid=t
        self.figures=figures

    def __str__(self):
        output=''
        for row in list(zip(*self._grid)):
            output+=''.join([str(c) for c in row])+'\n'
        return output

    def goal_test(self,ml):
        return self.king in self.successors(ml.state)

    def successors(self,ml):
        print('ML',ml)
        f=self._grid[ml.x][ml.y]
        if f.char=='♜':
            return self.check_rook(ml)
        elif f.char=='♝':
            return self.check_bishop(ml)
        elif f.char=='♛':
            return self.check_rook(ml)+self.check_bishop(ml)
        elif f.char=='♞':
            return self.check_knight(ml)
        elif f.char=='♟':
            return self.check_pawn(ml)



    def check_rook(self,ml):
        locations = []
        for i in range(self._columns+1):
            if i< self._columns-ml.y and self._grid[ml.x][ml.y+i].char not in ['♞','♝','♟']:
                locations.append(self._grid[ml.x][ml.y+i])
            else:
                break
        # print([l.state for l in locations])
        # input()
        for i in range(1,ml.y+1):
            if  ml.y-i >=0 and self._grid[ml.x][ml.y-i].char not in ['♞','♝','♟']:
                locations.append(self._grid[ml.x][ml.y - i])
            else:
                break
        # print([l.state for l in locations])
        # input()
        for i in range(1,ml.x+1):
            if ml.x-i>=0 and self._grid[ml.x-i][ml.y].char not in ['♞','♝','♟']:
                locations.append(self._grid[ml.x-i][ml.y])
            else:
                break
        # print([l.state for l in locations])
        # input()
        for i in range(self._rows+1):
            if i< self._rows - ml.x and self._grid[ml.x+i][ml.y].char not in ['♞','♝','♟']:
                locations.append(self._grid[ml.x + i][ml.y])
            else:
                break
        # print([l.state for l in locations])
        # input()
        return locations
    def check_pawn(self,ml):
        locations = []
        if ml.x==7:
            return self.check_bishop(ml)+self.check_rook(ml)
        else:
            if ml.y-1>=0:
                locations.append(self._grid[ml.x + 1][ml.y - 1])
            if ml.y+1<self._columns:
                locations.append(self._grid[ml.x + 1][ml.y + 1])
        return locations

    def check_bishop(self,ml):
        locations = []
        for i in range(self._rows+1):
            if i< self._rows-ml.x and i< self._columns-ml.y and self._grid[ml.x+i][ml.y+i].char not in ['♞','♜','♟']:
                locations.append(self._grid[ml.x+i][ml.y+i])
            else:
                break
        # print([l.state for l in locations])
        # input()
        for i in range(1,ml.x+1):
            if i <= self._rows and ml.y-i >=0 and self._grid[ml.x-i][ml.y-i].char not in ['♞','♜','♟']:
                locations.append(self._grid[ml.x - i][ml.y - i])
            else:
                break
        # print([l.state for l in locations])
        # input()
        for i in range(self._rows+1):
            if ml.x-i>=0 and i< self._columns-ml.y and self._grid[ml.x-i][ml.y+i].char not in ['♞','♜','♟']:
                locations.append(self._grid[ml.x-i][ml.y+i])
            else:
                break
        # print([l.state for l in locations])
        # input()
        for i in range(1,ml.y+1):
            if i + ml.x< self._rows and i < self._columns and self._grid[ml.x+i][ml.y-i].char not in ['♞','♜','♟']:
                locations.append(self._grid[ml.x + i][ml.y - i])
            else:
                break
        # print([l.state for l in locations])
        # input()
        return locations

    def check_knight(self,ml):
        locations=[]

        if ml.x+1<self._rows and ml.y-2>=0:
            locations.append(self._grid[ml.x+1][ml.y-2])
        print([l.state for l in locations])
        input()
        if ml.x+1<self._rows and ml.y+2<self._columns:
            locations.append(self._grid[ml.x+1][ml.y+2])
        print([l.state for l in locations])
        input()
        if ml.x+2<self._rows and ml.y-1>=0:
            locations.append(self._grid[ml.x+2][ml.y-1])
        print([l.state for l in locations])
        input()
        if ml.x+2<self._rows and ml.y+1<self._columns:
            locations.append(self._grid[ml.x+2][ml.y+1])
        print([l.state for l in locations])
        input()
        if ml.x-1>=0 and ml.y-2>=0:
            locations.append(self._grid[ml.x-1][ml.y-2])
        print([l.state for l in locations])
        input()
        if ml.x-1>=0 and ml.y+2<self._columns:
            locations.append(self._grid[ml.x-1][ml.y+2])
        print([l.state for l in locations])
        input()
        if ml.x-2>=0 and ml.y-1>=0:
            locations.append(self._grid[ml.x-2][ml.y-1])
        print([l.state for l in locations])
        input()
        if ml.x-2>=0 and ml.y+1<self._columns:
            locations.append(self._grid[ml.x-2][ml.y+1])
        print([l.state for l in locations])
        input()
        return locations

def king_is_in_check(chessboard):

    grid,king, figures = make_grid(chessboard)
    M=Maze(grid,king, figures)
    return checks(M.king, M.goal_test, M.successors,M._grid,M.figures)



def make_grid(chessboard):
    width=len(chessboard)
    height=len(chessboard[0])
    grid = []
    figures = []
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = chessboard[x][y]
            node = Figure(state=State(x, y), char=char)
            grid[x].append(node)
            if char!=' ' and char!='♔':
                figures.append(node)
            if char=='♔':
                king=node
    return grid,king,figures

def main():
    figures = ['♔','♛','♝','♞','♜','♟']

    chessboard=[
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♔',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ','♞',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ]

    print(king_is_in_check(chessboard))


    
    
  
    
if __name__ == "__main__":
    main()
