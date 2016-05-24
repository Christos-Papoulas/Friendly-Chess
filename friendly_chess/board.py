""" The board of chess. """

import copy

THREAT = 'T'


class Board(object):
    """ The board of chess and the logic of threating pieces. """

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
        return '\n'.join(['|'.join(
            ['{:4}'.format(i) if i != THREAT else '{:4}'.format(
                ' ') for i in row]) for row in self.board])

    def __eq__(self, other):
        """ Override the default Equals operator. """
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

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
        # assert self.board[x_pos][y_pos] == ' '
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
        for x_pos in range(0, self.sizeX):
            for y_pos in range(0, self.sizeY):
                if self.board[x_pos][y_pos] == 'K':
                    self.calculate_threats_for_king(x_pos, y_pos)
                elif self.board[x_pos][y_pos] == 'Q':
                    self.calculate_threats_for_queen(x_pos, y_pos)
                elif self.board[x_pos][y_pos] == 'B':
                    self.calculate_threats_for_bishop(x_pos, y_pos)
                elif self.board[x_pos][y_pos] == 'R':
                    self.calculate_threats_for_rook(x_pos, y_pos)
                elif self.board[x_pos][y_pos] == 'N':
                    self.calculate_threats_for_knight(x_pos, y_pos)

    def is_pawn_threats_others(self, pawn, x_pos, y_pos):
        """ Return True if the pawn in x, y threats any one else. """
        if pawn == 'K':
            return self.check_threats_for_king(x_pos, y_pos)
        elif pawn == 'Q':
            return self.check_threats_for_queen(x_pos, y_pos)
        elif pawn == 'B':
            return self.check_threats_for_bishop(x_pos, y_pos)
        elif pawn == 'R':
            return self.check_threats_for_rook(x_pos, y_pos)
        elif pawn == 'N':
            return self.check_threats_for_knight(x_pos, y_pos)
        assert True, "Unknown issue in is_pawn_threats_others"

    def calculate_threats_for_king(self, x_pos, y_pos):
        """ Add the threads to the board for the king. """
        for i in [-1, 0, 1]:
            if x_pos + i >= 0 and x_pos + i < self.sizeX:
                for j in [-1, 0, 1]:
                    if y_pos + j >= 0 and y_pos + j < self.sizeY:
                        self.set_position_as_thread(x_pos + i, y_pos + j)

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
        """ Add the threads to the board for the queen. """
        self.calculate_threats_for_bishop(x, y)
        self.calculate_threats_for_rook(x, y)
        return

    def calculate_threats_for_bishop(self, x_pos, y_pos):
        """ Add the threads to the board for the bishop. """
        dx_threats = [-1, -1, 1, 1]
        dy_threats = [-1, 1, -1, 1]
        b_threats = zip(dx_threats, dy_threats)
        for b_t in b_threats:
            for step in range(1, self.sizeX):
                p_x = x_pos + b_t[0] * step
                p_y = y_pos + b_t[1] * step
                if p_x >= 0 and p_x < self.sizeX and p_y >= 0 and p_y < self.sizeY:
                    self.set_position_as_thread(p_x, p_y)
        return

    def calculate_threats_for_knight(self, x_pos, y_pos):
        """ Add the threads to the board for the knight. """
        dx = [-2, -2, -1, 1, 2, 2, 1, -1]
        dy = [-1, 1, 2, 2, -1, 1, -2, -2]
        k_threats = zip(dx, dy)
        for t_pos in k_threats:
            t_x, t_y = t_pos
            px = x_pos + t_x
            py = y_pos + t_y
            if px >= 0 and px < self.sizeX and py >= 0 and py < self.sizeY:
                self.set_position_as_thread(px, py)
        return

    def check_threats_for_king(self, x_pos, y_pos):
        """ Return true if threat other pieces. """
        for i in [-1, 0, 1]:
            if x_pos + i >= 0 and x_pos + i < self.sizeX:
                for j in [-1, 0, 1]:
                    if y_pos + j >= 0 and y_pos + j < self.sizeY:
                        content = self.board[x_pos + i][y_pos + j]
                        if content != ' ' and content != THREAT:
                            return True
        return False

    def check_threats_for_rook(self, x_pos, y_pos):
        """ Return true if threat other pieces. """
        for i in range(0, self.sizeX):
            if self.board[i][y_pos] != ' ' and self.board[i][y_pos] != THREAT:
                return True

        for j in range(0, self.sizeY):
            if self.board[x_pos][j] != ' ' and self.board[x_pos][j] != THREAT:
                return True
        return False

    def check_threats_for_queen(self, x_pos, y_pos):
        """ Return true if threat other pieces. """
        return self.check_threats_for_rook(
            x_pos, y_pos) or self.check_threats_for_bishop(
            x_pos, y_pos)

    def check_threats_for_bishop(self, x_pos, y_pos):
        """ Return true if threat other pieces. """
        dx_threats = [-1, -1, 1, 1]
        dy_threats = [-1, 1, -1, 1]
        b_threats = zip(dx_threats, dy_threats)
        for bt in b_threats:
            for step in range(1, self.sizeX):
                px = x_pos + bt[0] * step
                py = y_pos + bt[1] * step
                if px >= 0 and px < self.sizeX and py >= 0 and py < self.sizeY:
                    if self.board[px][py] != ' ' and self.board[
                            px][py] != THREAT:
                        return True
        return False

    def check_threats_for_knight(self, x_pos, y_pos):
        """ Return true if threat other pieces. """
        dx_threats = [-2, -2, -1, 1, 2, 2, 1, -1]
        dy_threats = [-1, 1, 2, 2, -1, 1, -2, -2]
        k_threats = zip(dx_threats, dy_threats)
        for t_pos in k_threats:
            t_x, t_y = t_pos
            p_x = x_pos + t_x
            p_y = y_pos + t_y
            if p_x >= 0 and p_x < self.sizeX and p_y >= 0 and p_y < self.sizeY:
                if self.board[p_x][p_y] != ' ' and self.board[
                        p_x][p_y] != THREAT:
                    return True
        return False

    def rotated_boards(self):
        """ Return 3 new Boards rotated by 90, 180, 260 """
        new_board90 = copy.deepcopy(self)
        new_board180 = copy.deepcopy(self)
        new_board260 = copy.deepcopy(self)

        new_board90.change_board(zip(*self.board[::-1]))  # rotate
        new_board180.change_board(zip(*new_board90.board[::-1]))
        new_board260.change_board(zip(*new_board180.board[::-1]))

        return [new_board90, new_board180, new_board260]

    def get_pieces_and_positions(self):
        """ Return a list with the pieces and its positions. """
        pieces = []
        for i in range(self.sizeX):
            for j in range(self.sizeY):
                piece = self.board[i][j]
                if piece == ' ' or piece == 'T':
                    continue
                a_piece = {'p': piece, 'x': i, 'y': j}
                pieces.append(a_piece)
        return pieces
