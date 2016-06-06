#!/usr/bin/env python
""" Main script of FriendlyChess. """

from __future__ import print_function
from __future__ import absolute_import
from collections import Counter
import time
import copy
import sys
import ConfigParser

from friendly_chess.board import Board
from friendly_chess.pawn import King, Queen, Bishop, Knight, Rook


def main():
    """ Main of the project. """
    # read and check values
    config_parser = ConfigParser.RawConfigParser()
    config_filepath = r'chess.cfg'
    config_parser.read(config_filepath)

    size = config_parser.getint('chess', 'size')
    if size < 2:
        sys.stderr.write(
            "Please, provide a positive number as the size of board\n")
        return
    pieces = check_pieces(
        config_parser.get('chess', 'pieces').strip().split(' '))
    free_board = Board(size)
    solutions = []

    if size * size < len(pieces):
        print(
            "%d pieces don't fit in a %dx%d board" %
            (len(pieces), size, size))
        return

    # try to find solutions
    print("starting")

    start = time.time()
    find_solutions(free_board, pieces, solutions)
    end = time.time()

    print("finished")
    print("execution time: %.5f secs" % (end - start))

    print_solutions(solutions)
    return


def find_solutions(board, pieces, solutions):
    """ Find the solution'boards. """
    if len(pieces) == 0:
        if board not in solutions:
            solutions.append(board)
        rotated_brds = board.rotated_boards()
        for ro_board in rotated_brds:
            if ro_board not in solutions:
                solutions.append(ro_board)
        return

    for piece in pieces:
        pieces_new = pieces[:]
        pieces_new.remove(piece)  # remove the candidate

        secure_pos = board.get_secure_positions()
        if len(secure_pos) == 0:
            return

        for s_p in secure_pos:
            t_x, t_y = s_p
            if piece.check_threats(board, t_x, t_y) is True:
                continue

            new_board = copy.deepcopy(board)
            new_board.set_pawn_in(piece, t_x, t_y)  # set piece
            new_board.calculate_threats()
            if is_already_tried(new_board, solutions) is True:
                new_board.set_pawn_in(' ', t_x, t_y)  # unset piece
                continue

            find_solutions(new_board, pieces_new, solutions)

    return

def is_already_tried(board, solutions):
    """ Check in the solutions if this solution is tried and accepted. """
    current_pieces = board.get_pieces_and_positions()

    for sol in solutions:
        matches = 0
        for piece_pos in current_pieces:
            piece = piece_pos['p']
            p_x = piece_pos['x']
            p_y = piece_pos['y']
            if sol.board[p_x][p_y] == piece:
                matches = 1
        if matches == len(current_pieces):
            return True
    return False

def check_pieces(pieces):
    """ Check the pieces and return them.

    Return the pieces by frequency of occurrence.
    """
    accepted_pieces = ['K', 'Q', 'B', 'R', 'N']
    for piece in pieces:
        if piece not in accepted_pieces:
            mes = "%s not in accepted values, try one of the following " \
                "%s seperated by whitespace.\n" % (
                    piece, accepted_pieces)
            sys.stderr.write(mes)
            sys.exit()
    pieces.sort(key=Counter(pieces).get, reverse=True)
    class_pieces = []
    for piece in pieces:
        if piece == 'K':
            class_pieces.append(King())
        elif piece == 'Q':
            class_pieces.append(Queen())
        elif piece == 'B':
            class_pieces.append(Bishop())
        elif piece == 'R':
            class_pieces.append(Rook())
        elif piece == 'N':
            class_pieces.append(Knight())
    return class_pieces


def print_solutions(solutions):
    """ Iterate solutions and print them. """
    print("Found %d solutions: " % (len(solutions)))
    for sol in solutions:
        print(sol)

if __name__ == '__main__':
    main()
