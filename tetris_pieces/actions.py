# -*- coding: utf-8 -*-


class AbstractAction:

    def __init__(self, board, piece):
        self.board = board
        self._action = None
        self.piece = piece

    def position_piece(self):
        """
        Position a new piece to the middle top of the board
        :return: True if action is done else false if not possible
        """
        raise NotImplementedError

    def move_left(self):
        """
        Move the piece to the left of the board
        :return: True if action is done else false if not possible
        """
        raise NotImplementedError

    def move_right(self):
        """
        Move the piece to the Right of the board
        :return: True if action is done else false if not possible
        """
        raise NotImplementedError

    def rotate_clock_wise(self):
        """
        Rotate the piece clock wise in the board
        :return: True if action is done else false if not possible
        """
        raise NotImplementedError

    def rotate_counter_clock_wise(self):
        """
        Rotate the piece counter clock wise in the board
        :return: True if action is done else false if not possible
        """
        raise NotImplementedError

    def _check_board_full(self):
        """
        check if there is a room to put a new piece.
        this method should check the same board position where the piece
        would be positioned.
        :return:True if there is room for the piece else False
        """
        raise NotImplementedError


class IPieceAction(AbstractAction):

    def position_piece(self):
        if self._check_board_full():
            self.board.get_board()[1][self.board.width/2] = self.piece.get_piece()[1][len(self.piece.get_piece())/2]
            self.board.get_board()[1][(self.board.width/2) + 1] = self.piece.get_piece()[1][(len(self.piece.get_piece())/2) + 1]
            self.board.get_board()[1][(self.board.width/2) - 1] = self.piece.get_piece()[1][(len(self.piece.get_piece())/2) - 1]
            self.board.get_board()[1][(self.board.width/2) - 2] = self.piece.get_piece()[1][(len(self.piece.get_piece())/2) - 2]
            # Display the new board
            self.board.refresh_board()
            self.piece.x_position = (self.board.width/2 - 2)
            self.piece.y_position = 1
            return True

        return False

    def move_right(self):
        if self._check_move_right_valid():
            x = self.piece.x_position
            y = self.piece.y_position

            self.board.get_board()[y + 1][x+1] = '*'
            self.board.get_board()[y + 1][x+2] = '*'
            self.board.get_board()[y + 1][x+3] = '*'
            self.board.get_board()[y + 1][x+4] = '*'

            self.board.get_board()[y][x] = ' '
            self.board.get_board()[y][x + 1] = ' '
            self.board.get_board()[y][x + 2] = ' '
            self.board.get_board()[y][x + 3] = ' '

            self.piece.x_position = x + 4
            self.piece.y_position = y + 1
            self.board.refresh_board()

            return True
        return False

    def move_left(self):
        if self._check_move_left_valid():
            x = self.piece.x_position
            y = self.piece.y_position
            self.board.get_board()[y + 1][x-1] = '*'
            self.board.get_board()[y + 1][x] = '*'
            self.board.get_board()[y + 1][x + 1] = '*'
            self.board.get_board()[y + 1][x + 2] = '*'

            self.board.get_board()[y][x] = ' '
            self.board.get_board()[y][x + 1] = ' '
            self.board.get_board()[y][x + 2] = ' '
            self.board.get_board()[y][x + 3] = ' '

            self.piece.x_position = x - 1
            self.piece.y_position = y + 1
            self.board.refresh_board()
            return True
        return False

    def rotate_counter_clock_wise(self):
        return True

    def rotate_clock_wise(self):
        return True

    def _check_board_full(self):

        if self.board.get_board()[1][self.board.width/2] == ' ' and \
           self.board.get_board()[1][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[1][(self.board.width/2) - 1] == ' ' and \
           self.board.get_board()[1][(self.board.width/2) - 2] == ' ':
            return True
        else:
            False

    def _check_move_right_valid(self):

        x = self.piece.x_position
        y = self.piece.y_position

        if x-1 > 0:
            if self.board.get_board()[y + 1][x + 4] == ' ' and \
               self.board.get_board()[y + 1][x + 3] == ' ' and \
               self.board.get_board()[y + 1][x + 2] == ' ' and \
               self.board.get_board()[y + 1][x + 1] == ' ':
                return True
        return False

    def _check_move_left_valid(self):
        x = self.piece.x_position
        y = self.piece.y_position
        print x, y
        if x + 4 < len(self.board.get_board()) - 1:
            if self.board.get_board()[y + 1][x - 1] == ' ' and \
               self.board.get_board()[y + 1][x] == ' ' and \
               self.board.get_board()[y + 1][x + 1] == ' ' and \
               self.board.get_board()[y + 1][x + 2] == ' ':
                return True
        return False

class JPieceAction(AbstractAction):

    def position_piece(self):
        if self._check_board_full():
            self.board.get_board()[1][self.board.width/2] = self.piece.get_piece()[1][0]
            self.board.get_board()[1][(self.board.width/2) + 1] = self.piece.get_piece()[1][1]
            self.board.get_board()[2][(self.board.width/2)] = self.piece.get_piece()[2][0]
            self.board.get_board()[2][(self.board.width/2) + 1] = self.piece.get_piece()[2][1]
            self.board.get_board()[3][(self.board.width/2)] = self.piece.get_piece()[3][0]
            self.board.get_board()[3][(self.board.width/2) + 1] = self.piece.get_piece()[3][1]
            self.board.refresh_board()
            return True
        return False

    def move_right(self):
        return True

    def move_left(self):
        return True

    def rotate_counter_clock_wise(self):
        return True

    def rotate_clock_wise(self):
        return True

    def _check_board_full(self):

        if self.board.get_board()[1][self.board.width/2] == ' ' and \
           self.board.get_board()[1][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[2][(self.board.width/2)] == ' ' and \
           self.board.get_board()[2][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[3][(self.board.width/2)] == ' ' and \
           self.board.get_board()[3][(self.board.width/2) + 1] == ' ':
            return True
        else:
            return False


class LPieceAction(AbstractAction):

    def position_piece(self):
        if self._check_board_full():
            self.board.get_board()[1][self.board.width/2] = self.piece.get_piece()[1][0]
            self.board.get_board()[1][(self.board.width/2) + 1] = self.piece.get_piece()[1][1]
            self.board.get_board()[2][(self.board.width/2)] = self.piece.get_piece()[2][0]
            self.board.get_board()[2][(self.board.width/2) + 1] = self.piece.get_piece()[2][1]
            self.board.get_board()[3][(self.board.width/2)] = self.piece.get_piece()[3][0]
            self.board.get_board()[3][(self.board.width/2) + 1] = self.piece.get_piece()[3][1]
            self.board.refresh_board()
            return True
        return False

    def move_right(self):
        return True

    def move_left(self):
        return True

    def rotate_counter_clock_wise(self):
        return True

    def rotate_clock_wise(self):
        return True

    def _check_board_full(self):

        if self.board.get_board()[1][self.board.width/2] == ' ' and \
           self.board.get_board()[1][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[2][(self.board.width/2)] == ' ' and \
           self.board.get_board()[2][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[3][(self.board.width/2)] == ' ' and \
           self.board.get_board()[3][(self.board.width/2) + 1] == ' ':
            return True
        else:
            return False


class ZPieceAction(AbstractAction):

    def position_piece(self):
        if self._check_board_full():
            self.board.get_board()[1][self.board.width/2] = self.piece.get_piece()[1][0]
            self.board.get_board()[1][(self.board.width/2) + 1] = self.piece.get_piece()[1][1]
            self.board.get_board()[2][(self.board.width/2)] = self.piece.get_piece()[2][0]
            self.board.get_board()[2][(self.board.width/2) + 1] = self.piece.get_piece()[2][1]
            self.board.get_board()[3][(self.board.width/2)] = self.piece.get_piece()[3][0]
            self.board.get_board()[3][(self.board.width/2) + 1] = self.piece.get_piece()[3][1]
            self.board.refresh_board()
            return True

        return False

    def move_right(self):
        return True

    def move_left(self):
        return True

    def rotate_counter_clock_wise(self):
        return True

    def rotate_clock_wise(self):
        return True

    def _check_board_full(self):

        if self.board.get_board()[1][self.board.width/2] == ' ' and \
           self.board.get_board()[1][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[2][(self.board.width/2)] == ' ' and \
           self.board.get_board()[2][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[3][(self.board.width/2)] == ' ' and \
           self.board.get_board()[3][(self.board.width/2) + 1] == ' ':
            return True
        else:
            return False


class OPieceAction(AbstractAction):

    def position_piece(self):
        if self._check_board_full():
            self.board.get_board()[1][self.board.width/2] = self.piece.get_piece()[1][0]
            self.board.get_board()[1][(self.board.width/2) + 1] = self.piece.get_piece()[1][1]
            self.board.get_board()[2][(self.board.width/2)] = self.piece.get_piece()[2][0]
            self.board.get_board()[2][(self.board.width/2) + 1] = self.piece.get_piece()[2][1]
            self.piece.y_position = 1
            self.piece.x_position = self.board.width/2
            self.board.refresh_board()
            return True
        return False

    def move_left(self):
        if self._check_move_left_valid():
            x = self.piece.x_position
            y = self.piece.y_position
            self.board.get_board()[y + 1][x - 1] = '*'
            self.board.get_board()[y + 2][x] = '*'
            self.board.get_board()[y + 2][x - 1] = '*'

            self.board.get_board()[y][x] = ' '
            self.board.get_board()[y][x + 1] = ' '
            self.board.get_board()[y + 1][x + 1] = ' '

            # update position
            self.piece.y_position = y + 1
            self.piece.x_position = x - 1
            self.board.refresh_board()
            return True
        else:
            return False

    def move_right(self):
        if self._check_move_right_valid():
            x = self.piece.x_position
            y = self.piece.y_position
            self.board.get_board()[y + 2][x + 2] = '*'
            self.board.get_board()[y + 1][x + 2] = '*'
            self.board.get_board()[y + 1][x + 1] = '*'
            self.board.get_board()[y + 2][x + 1] = '*'

            self.board.get_board()[y][x] = ' '
            self.board.get_board()[y + 1][x] = ' '
            self.board.get_board()[y][x + 1] = ' '

            # update position
            self.piece.y_position = y + 1
            self.piece.x_position = x + 1
            self.board.refresh_board()
            return True
        else:
            return False

    def rotate_clock_wise(self):
        # a square don't need to be rotated return always true
        return True

    def rotate_counter_clock_wise(self):
        # a square don't need to be rotated return always true
        return True

    def _check_board_full(self):

        if self.board.get_board()[1][self.board.width/2] == ' ' and \
           self.board.get_board()[1][(self.board.width/2) + 1] == ' ' and \
           self.board.get_board()[2][(self.board.width/2)] == ' ' and \
           self.board.get_board()[2][(self.board.width/2) + 1]:
            return True
        return False

    def _check_move_right_valid(self):
        """
        Check if the action chosen by the player is valid
        :return: True if the action is valid else False
        """
        x = self.piece.x_position
        y = self.piece.y_position
        if (x + 1 < len(self.board.get_board()) - 1) and \
                (y + 1 < len(self.board.get_board()) - 1) and \
                (y + 2 < len(self.board.get_board()) - 1):
            print self.board.get_board()[y + 1][x + 2], self.board.get_board()[y + 2][x + 2], self.board.get_board()[y + 2][x + 2]
            if self.board.get_board()[y + 2][x + 2] == ' ' and  \
               self.board.get_board()[y + 1][x + 2] == ' ' and \
               self.board.get_board()[y + 2][x + 1] == ' ':
                return True
        return False

    def _check_move_left_valid(self):

        """
        Check if the action chosen by the player is valid
        :return: True if the action is valid else False
        """

        x = self.piece.x_position
        y = self.piece.y_position
        print x, y
        # Check if after the move the piece won't be outside the board
        if (x - 1 > 0) and \
                (y + 1 < len(self.board.get_board()) - 1) and \
                (y + 2 < len(self.board.get_board()) - 1):
                # if so check if the cells aren't full
                if self.board.get_board()[y + 1][x - 1] == ' ' and  \
                   self.board.get_board()[y + 2][x - 1] == ' ' and \
                   self.board.get_board()[y + 2][x - 1] == ' ':
                    return True

        return False
