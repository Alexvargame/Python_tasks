from minimax import find_best_move
from connectfour import C4Board
from board import Move,Board


board=C4Board()

def get_player_move():
    player_move=Move(-1)
    while player_move not in board.legal_moves:
        play=int(input("Enter a legal square (0-6):"))
        player_move=Move(play)
    return player_move

def main():
    board = C4Board()
    while True:
        human_move=get_player_move()
        board=board.move(human_move)
        if board.is_win:
            print('Human wins')
            break
        elif board.is_draw:
            print("Draw!")
            break
        computer_move=find_best_move(board,3)
        print(f'Computer move is {computer_move}')
        board=board.move(computer_move)
        print(board)
        if board.is_win:
            print('Computer wins')
            break
        elif board.is_draw:
            print('Draw')
            break



if __name__=="__main__":
    main()
