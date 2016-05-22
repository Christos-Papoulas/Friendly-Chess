""" The board of chess. """


class Board(object):
    """ The board of chess. """

    def __init__(self, M, N):
        """ Initiaze the board. """
        self.board = [[" " for _ in range(N)] for _ in range(M)]

    def __str__(self):
        """ Print the Board. """
        return '\n'.join(
            ['|'.join(['{:4}'.format(i) for i in row]) for row in self.board])

    def get_pawn_from(self, x_pos, y_pos):
        """ Return the pawn in position x_pos, y_pos or None. """
        return self.board[x_pos][y_pos]

    def set_pawn_in(self, pawn, x_pos, y_pos):
        """ Set the pawn in position x_pos, y_pos. """
        self.board[x_pos][y_pos] = pawn
