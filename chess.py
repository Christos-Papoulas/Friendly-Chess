#!/usr/bin/env python
""" Main script of FriendlyChess. """

from __future__ import print_function
from __future__ import absolute_import
from collections import Counter
import time
import copy
import sys
import ConfigParser
#import pdb

from friendly_chess.board import Board


def main():
    """ Main of the project. """
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
    free_board = Board(size, size)
    solutions = []

    if size * size < len(pieces):
        print(
            "%d pieces don't fit in a %dx%d board" %
            (len(pieces), size, size))
        return

    print("starting")

    start = time.time()
    find_solutions(free_board, pieces, solutions, 0)
    end = time.time()

    print("finished")
    print("execution time: %.5f secs" % (end - start))

    print_solutions(solutions)
    return


def find_solutions(board, pieces, solutions, num):
    """ Find the boards. """
    if len(pieces) == 0:
        solutions.append(board)
        rotated_brds = board.rotated_boards()
        for a_board in rotated_brds:
            if a_board not in solutions:
                solutions.append(a_board)
        return

    for piece in pieces:
        pieces_new = pieces[:]
        pieces_new.remove(piece)  # remove the candidate

        secure_pos = board.get_secure_positions()
        if len(secure_pos) == 0:
            return

        for s_p in secure_pos:
            t_x, t_y = s_p
            if board.is_pawn_threats_others(piece, t_x, t_y) is True:
                continue

            new_board = copy.deepcopy(board)
            new_board.set_pawn_in(piece, t_x, t_y)  # set piece
            if is_already_tried(new_board, solutions) is True:
                new_board.set_pawn_in(' ', t_x, t_y)  # unset piece
                continue

            new_board.calculate_threats()
            find_solutions(new_board, pieces_new, solutions, num + 1)
    return


def is_already_tried(board, solutions):
    """ Check in the solutions if this solution is tried and accepted. """
    # for sol in solutions:
    #     if sol.board[x_pos][y_pos] == piece:
    #         return True
    current_pieces = board.get_pieces_and_positions()
    # pdb.set_trace()

    for sol in solutions:
        matches = 0
        for piece_pos in current_pieces:
            piece = piece_pos['p']
            p_x = piece_pos['x']
            p_y = piece_pos['y']
            if sol.board[p_x][p_y] == piece:
                matches += 1
        if matches == len(current_pieces):
            return True
    # pdb.set_trace()
    return False


def check_pieces(pieces):
    """ Check the pieces and return them.

    Return the pieces by frequency of occurrence.
    """
    accepted_pieces = ['K', 'Q', 'B', 'R', 'N']
    for piece in pieces:
        if piece not in accepted_pieces:
            mes = "%s not in accepted values, try one of the following %s seperated by whitespace.\n" % (
                piece, accepted_pieces)
            sys.stderr.write(mes)
            sys.exit()
    pieces.sort(key=Counter(pieces).get, reverse=True)
    return pieces


def print_solutions(solutions):
    """ Iterate solutions and print them. """
    print("Found %d solutions: " % (len(solutions)))
    for sol in solutions:
        print(sol)
        print("\n")

if __name__ == '__main__':
    main()
