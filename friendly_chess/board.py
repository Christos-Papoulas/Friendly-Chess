""" The board of chess. """

THREAT = 'T'
import pdb


class Board(object):
    """ The board of chess and the logic of threating pieces. """

    def __init__(self, size, data=None):
        """ Initiaze the board. """
        if data is None:
            self.board = [[" " for _ in range(size)] for _ in range(size)]
        else:
            self.board = data
        self.size = size

    def __str__(self):
        """ Print the Board. """
        def outer_join(sep, piece):
            """ Like join but enclose the result with outer separators. """
            return "%s%s%s" % (sep, sep.join(piece), sep)
        print_board = ""
        divider = outer_join("+", "-" * self.size) + "\n"
        print_board += divider
        for row in range(self.size):
            print_board += outer_join(
                "|", [' ' if i == 'T' else str(i) for i in self.board[
                    row]]) + "\n"
            print_board += divider
        return print_board

    def __eq__(self, other):
        """ Override the default Equals operator. """
        return (isinstance(other, self.__class__)
                and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        """ Override the default non-equality operator. """
        return not self.__eq__(other)

    def change_board(self, data):
        """ Update the board with a new one. """
        self.board = data

    def get_pawn_from(self, x_pos, y_pos):
        """ Return the pawn in position x_pos, y_pos or None. """
        return self.board[x_pos][y_pos]

    def set_pawn_in(self, pawn, x_pos, y_pos):
        """ Set the pawn in position x_pos, y_pos. """
        self.board[x_pos][y_pos] = pawn

    def get_secure_positions(self):
        """ Return all free positions. """
        self.calculate_threats()
        return [(ix, iy) for ix, row in enumerate(self.board)
                for iy, i in enumerate(row) if i == ' ']

    def set_position_as_thread(self, x_pos, y_pos):
        """ Set the position x_pos, y_pos as thread. """
        if self.board[x_pos][y_pos] == ' ':
            self.board[x_pos][y_pos] = THREAT

    def calculate_threats(self):
        """ Add the threts to the board. """
        for x_pos in range(0, self.size):
            for y_pos in range(0, self.size):
                    if self.board[x_pos][y_pos] != ' ':
                        if self.board[x_pos][y_pos] != THREAT:
                            self.board[x_pos][y_pos].calculate_threats(
                                self, x_pos, y_pos)

    def rotated_boards(self):
        """ Return the rotated and symmetry boards. """
        def transform_to_list(board):
            """ Get a board and change tuples to lists. """
            itr = 0
            for row in board:
                board[itr] = list(row)
                itr += 1
            return board
        # rotated boards
        new_board90 = Board(self.size)
        new_board180 = Board(self.size)
        new_board260 = Board(self.size)

        new_board90.change_board(transform_to_list(
            zip(*self.board[::-1])))  # rotate
        new_board180.change_board(
            transform_to_list(zip(*new_board90.board[::-1])))
        new_board260.change_board(
            transform_to_list(zip(*new_board180.board[::-1])))

        return [new_board90, new_board180, new_board260]
