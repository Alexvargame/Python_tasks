
from collections import defaultdict
def isValidSudoku(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    boxes = defaultdict(set)

    for ind_row, row in enumerate(board):
        for ind_col, el in enumerate(row):
            if el == '.':
                continue
            ind_box = (ind_row//3, ind_col//3)
            if (el in cols[ind_col]
                or el in rows[ind_row]
                or el in boxes[ind_box]
            ):
                return False
            cols[ind_col].add(el)
            rows[ind_row].add(el)
            boxes[ind_box].add(el)
    return True
def main():
    print('res', isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))



if __name__ == "__main__":
    main()
