""" The pawn class. All pawns inherite this class. """

THREAT = 'T'


class Pawn(object):
    """ The basic class for all pawns. """
    def __init__(self):
        pass

    def __str__(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @classmethod
    def calculate_threats(cls, board, x_pos, y_pos):
        """ Add the threads to the board. """
        raise NotImplementedError("Subclass must implement abstract method")

    @classmethod
    def check_threats(cls, board, x_pos, y_pos):
        """ Return true if threat other pieces. """
        raise NotImplementedError("Subclass must implement abstract method")

    def __eq__(self, other):
        """ Override the default Equals operator. """
        raise NotImplementedError("Subclass must call this method")

    def __ne__(self, other):
        """ Override the default non-equality operator. """
        raise NotImplementedError("Subclass must call this method")


class King(Pawn):
    """ The class with all the logic for King. """
    @classmethod
    def calculate_threats(cls, board, x_pos, y_pos):
        """ Add the threads to the board for the king.

        Args:
            board: the chess board.
            x_pos: the row position of King.
            x_pos: the column position of King.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        for i in [-1, 0, 1]:
            if x_pos + i >= 0 and x_pos + i < board.size:
                for j in [-1, 0, 1]:
                    if y_pos + j >= 0 and y_pos + j < board.size:
                        board.set_position_as_thread(x_pos + i, y_pos + j)
        return

    @classmethod
    def check_threats(cls, board, x_pos, y_pos):
        """ Return true if threat other pieces.

        Args:
            board: the chess board.
            x_pos: the row position of Rook.
            x_pos: the column position of Rook.
        Returns:
            True if the Rook threats other pieces.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        for i in [-1, 0, 1]:
            if x_pos + i >= 0 and x_pos + i < board.size:
                for j in [-1, 0, 1]:
                    if y_pos + j >= 0 and y_pos + j < board.size:
                        content = board.board[x_pos + i][y_pos + j]
                        if content != ' ' and content != THREAT:
                            return True
        return False

    def __str__(self):
        """ Return the string representation for the King. """
        return 'K'

    def __eq__(self, other):
        """ Override the default Equals operator. """
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        """ Override the default non-equality operator. """
        return not self.__eq__(other)


class Queen(Pawn):
    """ The class with all the logic for Queen. """
    @classmethod
    def calculate_threats(cls, board, x_pos, y_pos):
        """ Add the threats to the board for the Queen.

        The Queen threats are a combination of Bishop and
        Rook threats.

        Args:
            board: the chess board.
            x_pos: the row position of Queen.
            x_pos: the column position of Queen.
        """
        Bishop.calculate_threats(board, x_pos, y_pos)
        Rook.calculate_threats(board, x_pos, y_pos)
        return

    @classmethod
    def check_threats(cls, board, x_pos, y_pos):
        """ Return true if threat other pieces.

        The Queen threats are a combination of Bishop and
        Rook threats.

        Args:
            board: the chess board.
            x_pos: the row position of Queen.
            x_pos: the column position of Queen.
        Returns:
            True if the Queen threats other pieces.
        """
        return Rook.check_threats(
            board, x_pos, y_pos) or Bishop.check_threats(
            board, x_pos, y_pos)

    def __str__(self):
        """ Return the string representation for the Queen. """
        return 'Q'

    def __eq__(self, other):
        """ Override the default Equals operator. """
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        """ Override the default non-equality operator. """
        return not self.__eq__(other)


class Bishop(Pawn):
    """ The class with all the logic for Bishop. """
    @classmethod
    def calculate_threats(cls, board, x_pos, y_pos):
        """ Add the threads to the board for the bishop.

        Args:
            board: the chess board.
            x_pos: the row position of Bishop.
            x_pos: the column position of Bishop.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        dx_threats = [-1, -1, 1, 1]
        dy_threats = [-1, 1, -1, 1]
        b_threats = zip(dx_threats, dy_threats)
        for b_t in b_threats:
            for step in range(1, board.size):
                p_x = x_pos + b_t[0] * step
                p_y = y_pos + b_t[1] * step
                if p_x >= 0 and p_x < board.size and \
                    p_y >= 0 and p_y < board.size:
                    board.set_position_as_thread(p_x, p_y)

    @classmethod
    def check_threats(cls, board, x_pos, y_pos):
        """ Return true if threat other pieces.

        Args:
            board: the chess board.
            x_pos: the row position of Bishop.
            x_pos: the column position of Bishop.
        Returns:
            True if the Bishop threats other pieces.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        dx_threats = [-1, -1, 1, 1]
        dy_threats = [-1, 1, -1, 1]
        b_threats = zip(dx_threats, dy_threats)
        for b_t in b_threats:
            for step in range(1, board.size):
                px = x_pos + b_t[0] * step
                py = y_pos + b_t[1] * step
                if px >= 0 and px < board.size and py >= 0 and py < board.size:
                    if board.board[px][py] != ' ' and board.board[
                            px][py] != THREAT:
                        return True
        return False

    def __str__(self):
        """ Return the string representation for the Bishop. """
        return 'B'

    def __eq__(self, other):
        """ Override the default Equals operator. """
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        """ Override the default non-equality operator. """
        return not self.__eq__(other)


class Knight(Pawn):
    """ The class with all the logic for Knight. """
    @classmethod
    def calculate_threats(cls, board, x_pos, y_pos):
        """ Add the threads to the board for the knight.

        Args:
            board: the chess board.
            x_pos: the row position of Knight.
            x_pos: the column position of Knight.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        dx = [-2, -2, -1, 1, 2, 2, 1, -1]
        dy = [-1, 1, 2, 2, -1, 1, -2, -2]
        k_threats = zip(dx, dy)
        for t_pos in k_threats:
            t_x, t_y = t_pos
            px = x_pos + t_x
            py = y_pos + t_y
            if px >= 0 and px < board.size and py >= 0 and py < board.size:
                board.set_position_as_thread(px, py)

    @classmethod
    def check_threats(cls, board, x_pos, y_pos):
        """ Return true if threat other pieces.

        Args:
            board: the chess board.
            x_pos: the row position of Knight.
            x_pos: the column position of Knight.
        Returns:
            True if the Knight threats other pieces.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        dx_threats = [-2, -2, -1, 1, 2, 2, 1, -1]
        dy_threats = [-1, 1, 2, 2, -1, 1, -2, -2]
        k_threats = zip(dx_threats, dy_threats)
        for t_pos in k_threats:
            t_x, t_y = t_pos
            p_x = x_pos + t_x
            p_y = y_pos + t_y
            if p_x >= 0 and p_x < board.size and p_y >= 0 and p_y < board.size:
                if board.board[p_x][p_y] != ' ' and board.board[
                        p_x][p_y] != THREAT:
                    return True
        return False

    def __str__(self):
        """ Return the string representation for the Knight. """
        return 'N'

    def __eq__(self, other):
        """ Override the default Equals operator. """
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        """ Override the default non-equality operator. """
        return not self.__eq__(other)


class Rook(Pawn):
    """ The class with all the logic for Rook. """
    @classmethod
    def calculate_threats(cls, board, x_pos, y_pos):
        """ Add the threads to the board for the Rook.

        Args:
            board: the chess board.
            x_pos: the row position of Rook.
            x_pos: the column position of Rook.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        for i in range(0, board.size):
            # print("i: " + str(i))
            if board.board[i][y_pos] == ' ':
                board.set_position_as_thread(i, y_pos)

        for j in range(0, board.size):
            # print("j: " + str(j))
            if board.board[x_pos][j] == ' ':
                board.set_position_as_thread(x_pos, j)

    @classmethod
    def check_threats(cls, board, x_pos, y_pos):
        """ Return true if threat other pieces.

        Args:
            board: the chess board.
            x_pos: the row position of Rook.
            x_pos: the column position of Rook.
        Returns:
            True if the Rook threats other pieces.
        Raises:
            IndexError: If x_pos or y_pos are not valid.
        """
        if x_pos > board.size or y_pos > board.size:
            raise IndexError('potition is out of board size')
        for i in range(0, board.size):
            if board.board[i][y_pos] != ' ' and board.board[
                    i][y_pos] != THREAT:
                return True

        for j in range(0, board.size):
            if board.board[x_pos][j] != ' ' and board.board[
                    x_pos][j] != THREAT:
                return True
        return False

    def __str__(self):
        """ Return the string representation for the Rook. """
        return 'R'

    def __eq__(self, other):
        """ Override the default Equals operator. """
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        """ Override the default non-equality operator. """
        return not self.__eq__(other)
