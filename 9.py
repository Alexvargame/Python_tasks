import math
from datetime import *


coor = input()
board = [['.'] * 8 for _ in range(8)]
y, x = 8 - int(coor[1]), ord(coor[0]) - 97
for i in range(8):
    for j in range(8):
        if (y == i) or (x == j) or abs(y - i) == abs(x - j):
            board[i][j] = '*'
board[y][x] = 'Q'
for line in board:
    print(*line)
