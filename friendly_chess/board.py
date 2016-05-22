""" The board of chess. """

THREAT = 'T'


class Board(object):
    """ The board of chess. """

    def __init__(self, M, N, data=None):
        """ Initiaze the board. """
        if data is None:
            self.board = [[" " for _ in range(N)] for _ in range(M)]
        else:
            self.board = data
        self.sizeX = M
        self.sizeY = N

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
        for x in range(0, self.sizeX):
            for y in range(0, self.sizeY):
                if self.board[x][y] == 'K':
                    self.calculate_threats_for_king(x, y)
                elif self.board[x][y] == 'Q':
                    self.calculate_threats_for_queen(x, y)
                elif self.board[x][y] == 'B':
                    self.calculate_threats_for_bishop(x, y)
                elif self.board[x][y] == 'R':
                    self.calculate_threats_for_rook(x, y)
                elif self.board[x][y] == 'N':
                    self.calculate_threats_for_knight(x, y)

    def is_pawn_threats_others(self, pawn, x, y):
        """ Return True if the pawn in x, y threats any one else. """
        if pawn == 'K':
            return self.check_threats_for_king(x, y)
        elif pawn == 'Q':
            return self.check_threats_for_queen(x, y)
        elif pawn == 'B':
            return self.check_threats_for_bishop(x, y)
        elif pawn == 'R':
            return self.check_threats_for_rook(x, y)
        elif pawn == 'N':
            return self.check_threats_for_knight(x, y)
        assert True, "Unknown issue in is_pawn_threats_others"

    def calculate_threats_for_king(self, x, y):
        """ Add the threads to the board for the king. """
        for i in [-1, 0, 1]:
            if x + i >= 0 and x + i < self.sizeX:
                for j in [-1, 0, 1]:
                    if y + j >= 0 and y + j < self.sizeY:
                        self.set_position_as_thread(x + i, y + j)

    def calculate_threats_for_rook(self, x, y):
        """ Add the threads to the board. """
        for i in range(0, self.sizeX):
            # print("i: " + str(i))
            if self.board[i][y] == ' ':
                self.set_position_as_thread(i, y)

        for j in range(0, self.sizeY):
            # print("j: " + str(j))
            if self.board[x][j] == ' ':
                self.set_position_as_thread(x, j)
        return

    def calculate_threats_for_queen(self, x, y):
        """ Add the threads to the board. """
        assert True, "Not implemented"
        return

    def calculate_threats_for_bishop(self, x, y):
        """ Add the threads to the board. """
        assert True, "Not implemented"
        return

    def calculate_threats_for_knight(self, x, y):
        """ Add the threads to the board. """
        assert True, "Not implemented"
        return

    def check_threats_for_king(self, x, y):
        """ Return true if threat other pawns. """
        for i in [-1, 0, 1]:
            if x + i >= 0 and x + i < self.sizeX:
                for j in [-1, 0, 1]:
                    if y + j >= 0 and y + j < self.sizeY:
                        content = self.board[x + i][y + j]
                        if content != ' ' and content != THREAT:
                            return True
        return False

    def check_threats_for_rook(self, x, y):
        """ Return true if threat other pawns. """
        for i in range(0, self.sizeX):
            # print("i: " + str(i))
            if self.board[i][y] != ' ' and self.board[i][y] != THREAT:
                return True

        for j in range(0, self.sizeY):
            # print("j: " + str(j))
            if self.board[x][j] != ' ' and self.board[x][j] != THREAT:
                return True
        return False

    def check_threats_for_queen(self, x, y):
        """ Return true if threat other pawns. """
        assert True, "Not implemented"
        return

    def check_threats_for_bishop(self, x, y):
        """ Return true if threat other pawns. """
        assert True, "Not implemented"
        return

    def check_threats_for_knight(self, x, y):
        """ Return true if threat other pawns. """
        assert True, "Not implemented"
        return
