
def back_track(row, n, occupied_cols, occupied_neg_diag, occupied_pos_diag, board):
    if row == n:
        res += 1
        return
    for col in range(n):
        pos_idx = row + col
        neg_idx = row - col
        if (
            col in occupied_cols
            or
            pos_idx in occupied_pos_diag
            or
            neg_idx in occupied_neg_diag
        ):
            continue
        occupied_cols.add(col)
        occupied_neg_diag.add(neg_idx)
        occupied_pos_diag.add(pos_idx)
        board[row][col] = "Q"
        back_track(row + 1, n, occupied_cols, occupied_neg_diag, occupied_pos_diag, board, res)
        board[row][col] = "."

        occupied_cols.remove(col)
        occupied_neg_diag.remove(neg_idx)
        occupied_pos_diag.remove(pos_idx)
def totalNQeens(n):
    occupied_cols = set()
    occupied_pos_diag = set()
    occupied_neg_diag = set()

    board = [["."] * n for _ in range(n)]
    res = 0
    back_track(0, n, occupied_cols, occupied_neg_diag, occupied_pos_diag, board, res)

    return res


def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', totalNQeens(4))



if __name__ == "__main__":
    main()
