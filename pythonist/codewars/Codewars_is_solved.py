
def diag(board):
    first=board[0][0]
    for i in range(1,len(board)):
        if board[i][i]!=first:
            return False
        
    return first

    
        
            
def is_solved(board):
    print(diag(board))
    board_t=list(zip(*board[::-1]))
    print(diag(board_t))
    print(board_t, [list(set(b)) for b in board_t if len(set(b))==1],[all(board[i]) for i in range(len(board))])
    
    
    if ([1] in [list(set(b)) for b in board if len(set(b))==1]) or ([1] in [list(set(b)) for b in board_t if len(set(b))==1]) or diag(board)==1 or diag(board_t)==1:
        return 1
    elif ([2] in [list(set(b)) for b in board if len(set(b))==1]) or ([2] in [list(set(b)) for b in board_t if len(set(b))==1]) or diag(board)==2 or diag(board_t)==2:
        return 2
    elif False in [all(board[i]) for i in range(len(board))]:
        print('f')
        return -1
    return 0
    board_t=list(zip(*board[::-1]))
    
    

def main():
    print(is_solved([[1, 2, 0], [0, 1, 2], [0, 0, 1]]))
    

if __name__ == "__main__":
    main()

#
