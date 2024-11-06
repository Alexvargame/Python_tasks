
def dfs(row, col, idx, path, word, board):
    if idx == len(word):
        return True
    key = row, col
    if (row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or
            word[idx] != board[row][col] or key in path):
        return False
    path.add(key)
    res = False
    for r, c in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if dfs(row + r, col + c, idx + 1, path, word, board):
            res = True

    path.remove(key)
    return res
def exists(board, word):
    rows = len(board)
    cols = len(board[0])
    path = set()
    for row in range(rows):
        for col in range(cols):
            if dfs(row, col, 0, path, word, board):
                return True


    return False


def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', exists(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCEU"))



if __name__ == "__main__":
    main()
