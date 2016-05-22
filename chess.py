#!/usr/bin/env python
""" Main script of FriendlyChess. """

from __future__ import print_function
from __future__ import absolute_import
from friendly_chess.board import Board
import time
import copy


def main():
    """ Main of the project. """
    M = 4
    N = 4
    pawns = ['N', 'N', 'N', 'N', 'R', 'R']
    free_board = Board(M, N)
    solutions = []

    start = time.time()
    print("starting")
    find_solutions(free_board, pawns, M, N, solutions, 0)
    end = time.time()
    print("finished")
    print("execution time: %.5f secs" % (end - start))

    print("Found %d solutions: " % (len(solutions)))
    for s in solutions:
        print(s)
        print("\n")
    return


def find_solutions(board, pawns, M, N, solutions, num):
    """ Find the boards. """
    # print(board)
    # print("called with pawns: ")
    # print(pawns)
    # print("recursion: %d" % (num))
    # raw_input('continue:')

    if len(pawns) == 0:
        solutions.append(board)
        return True

    pi = 0
    for p in pawns:
        pi += 1  # count tried pawns

        pawns_new = pawns[:]
        pawns_new.remove(p)  # remove the candidate

        secure_pos = board.get_secure_positions()
        if len(secure_pos) == 0:
            return

        for s in secure_pos:
            tx, ty = s
            if board.is_pawn_threats_others(p, tx, ty) is True:
                continue
            if is_already_tried(p, tx, ty, solutions) is True:
                continue

            b = copy.deepcopy(board)
            b.set_pawn_in(p, tx, ty)
            b.calculate_threats()
            res = find_solutions(b, pawns_new, M, N, solutions, num + 1)
    return False


def is_already_tried(p, tx, ty, solutions):
    """ Check in the solutions if this position is tried and accepted. """
    for s in solutions:
        if s.board[tx][ty] == p:
            return True
    return False

if __name__ == '__main__':
    main()
