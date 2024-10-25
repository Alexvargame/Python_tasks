from __future__ import annotations

import unittest
from typing import List
from minimax import find_best_move
from board import Move
from tictactoe import TTTPiece,TTTBoard



class TTTMinimax(unittest.TestCase):
    def test_easy_position(self):
        to_win_easy_position=[TTTPiece.X,TTTPiece.O,TTTPiece.X,
                              TTTPiece.X,TTTPiece.E,TTTPiece.O,
                              TTTPiece.E,TTTPiece.E,TTTPiece.O]

        test_board1=TTTBoard(to_win_easy_position,TTTPiece.X)
        answer1=find_best_move(test_board1)
        self.assertEquals(answer1,6)
    def test_block_position(self):
        to_block_position=[TTTPiece.X,TTTPiece.E,TTTPiece.E,
                              TTTPiece.E,TTTPiece.E,TTTPiece.O,
                              TTTPiece.E,TTTPiece.X,TTTPiece.O]
        test_board2=TTTBoard(to_block_position,TTTPiece.X)
        answer2=find_best_move(test_board2)
        self.assertEquals(answer2,2)
    def test_hard_position(self):
        to_win_hard_position=[TTTPiece.X,TTTPiece.E,TTTPiece.E,
                              TTTPiece.E,TTTPiece.E,TTTPiece.O,
                              TTTPiece.O,TTTPiece.X,TTTPiece.E]
        test_board3=TTTBoard(to_win_hard_position,TTTPiece.X)
        answer3=find_best_move(test_board3)
        self.assertEquals(answer3,1)
def main():
    unittest.main()



if __name__=="__main__":
    main()
