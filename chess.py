#!/usr/bin/env python
""" Main script of FriendlyChess. """

from __future__ import print_function
from __future__ import absolute_import
from friendly_chess.board import Board
import time
import copy
import ConfigParser


def main():
    """ Main of the project. """
    configParser = ConfigParser.RawConfigParser()
    configFilePath = r'chess.cfg'
    configParser.read(configFilePath)

    size = configParser.getint('chess', 'size')
    pieces = configParser.get('chess', 'pieces').strip().split(' ')
    free_board = Board(size, size)
    solutions = []

    start = time.time()
    print("starting")
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
            if is_already_tried(piece, t_x, t_y, solutions) is True:
                continue

            new_board = copy.deepcopy(board)
            new_board.set_pawn_in(piece, t_x, t_y)
            new_board.calculate_threats()
            find_solutions(new_board, pieces_new, solutions, num + 1)
    return


def is_already_tried(piece, x_pos, y_pos, solutions):
    """ Check in the solutions if this position is tried and accepted. """
    for sol in solutions:
        if sol.board[x_pos][y_pos] == piece:
            return True
    return False


def print_solutions(solutions):
    """ Iterate solutions and print them. """
    print("Found %d solutions: " % (len(solutions)))
    for sol in solutions:
        print(sol)
        print("\n")

if __name__ == '__main__':
    main()
