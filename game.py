# -*- coding: utf-8 -*-
from tetris_board.board import TetrisBoard
from tetris_pieces.pieces import (IPieceFactory, JPieceFactory, LPieceFactory, ZPieceFactory, OPieceFactory)
import numpy as np

TETRIS_PIECES = {0: IPieceFactory, 1: JPieceFactory, 2: LPieceFactory, 3: ZPieceFactory, 4: OPieceFactory}


def next_piece():
    random_piece = np.random.randint(len(TETRIS_PIECES))
    print "Random Piece", random_piece
    return TETRIS_PIECES[0]()


def nex_action(input_var, piece_action):
    if input_var in ['s', 'S', 'd', 'D', 'a', 'A', 'w','W']:
        if input_var in ['s', 'S']:
            result = piece_action.rotate_clock_wise()
        elif input_var in ['d', 'D']:
            result = piece_action.move_right()
        elif input_var in ['a', 'A']:
            print "moving left"
            result = piece_action.move_left()
        elif input_var in ['w', 'W']:
            result = piece_action.rotate_counter_clock_wise()
        if result:
            input_var = raw_input("Enter something: ")
            print ("you entered " + input_var)
            nex_action(input_var, piece_action)
        else:
            print "False"
            return False
    else:
        input_var = raw_input("You have Entered a Wrong Action, Enter something else: ")
        nex_action(input_var, piece_action)


def main():
    board_size = '20x20'
    if 'x' in board_size:
        length, width = board_size.split('x')
        game_board = TetrisBoard(length=int(length), width=int(width))
        print "The has started, good luck!"
        game_board.refresh_board()
        while True:
            # Randomly create a new piece
            piece_factory = next_piece()
            new_piece = piece_factory.get_piece()
            # choose the right action handler depending the piece type
            piece_action = piece_factory.get_action(piece=new_piece, board=game_board)
            # position the piece in the top mid of the board
            result = piece_action.position_piece()
            if not result:
                print "Game Over"
                break
            input_var = raw_input("Enter something: ")
            print ("you entered " + input_var)
            nex_action(input_var, piece_action)


if __name__ == "__main__":
    main()
