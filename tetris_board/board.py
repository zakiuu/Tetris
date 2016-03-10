# -*- coding: utf-8 -*-


class TetrisBoard:

    def __init__(self, width, length):

        self._width = width
        self._length = length
        self._board = self._init_board()

    def refresh_board(self):
        for index in self._board:
            line = ''
            for element in self._board[index]:
                line += element
            print line
        return True

    def _init_board(self):
        board = {}
        i = 1
        while i < self._length:
            board.update({i: [' ' for j in range(self._width - 2)]})
            board[i].insert(0, '*')
            board[i].insert(self._width - 1, '*')
            i += 1
            board.update({i: ['*' for j in range(self._width)]})
        return board

    def _game_over(self):
        return False

    def get_board(self):
        return self._board

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

