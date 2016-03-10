# -*- coding: utf-8 -*-
from actions import *


class TetrisPiece:

    def __init__(self):
        self._piece = self._init_piece()

        # the column number of the left top cell of the piece in the board

        self._x_position = None

        # the row number of the left top cell of the piece in the board
        self._y_position = None

    def _init_piece(self):
        raise NotImplementedError

    def get_piece(self):
        return self._piece

    @property
    def x_position(self):
        return self._x_position

    @property
    def y_position(self):
        return self._y_position


class IPiece(TetrisPiece):
    def _init_piece(self):
        return {1: ['*', '*', '*', '*']}


class JPiece(TetrisPiece):
    def _init_piece(self):
        return {1: [' ', '*'],
                2: [' ', '*'],
                3: ['*', '*']}


class LPiece(TetrisPiece):
    def _init_piece(self):
        return {1: ['*', ' '],
                2: ['*', ' '],
                3: ['*', '*']}

class ZPiece(TetrisPiece):
    def _init_piece(self):
        return {1: [' ', '* '],
                2: ['*', '* '],
                3: ['*', ' ']}


class OPiece(TetrisPiece):
    def _init_piece(self):
        return {1: ['*', '* '],
                2: ['*', '* ']}


class IPieceFactory(object):

    def get_piece(self):
        return IPiece()

    def get_action(self, piece, board):
        return IPieceAction(piece=piece, board=board)


class JPieceFactory(object):
    def get_piece(self):
        return JPiece()

    def get_action(self, piece, board):
        return JPieceAction(piece=piece, board=board)


class LPieceFactory(object):
    def get_piece(self):
        return LPiece()

    def get_action(self, piece, board):
        return LPieceAction(piece=piece, board=board)


class ZPieceFactory(object):
    def get_piece(self):
        return ZPiece()

    def get_action(self, piece, board):
        return ZPieceAction(piece=piece, board=board)


class OPieceFactory(object):
    def get_piece(self):
        return OPiece()

    def get_action(self, piece, board):
        return OPieceAction(piece=piece, board=board)




