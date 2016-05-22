#!/usr/bin/env python
""" Main script of FriendlyChess. """

from __future__ import print_function
from __future__ import absolute_import
from friendly_chess.board import Board


def main():
    """ Main of the project. """
    print("started")
    M = 3
    N = 3
    free_board = Board(M, N)
    pawns = ['K', 'K', 'R']
    findSolutions(free_board, pawns, M, N)
    print("finished")
    return


def findSolutions(board, pawns, M, N):
    """ Find the solution boards. """
    if len(pawns) == 0:
        print(board)
        print('\n')
        return

    b = None
    for p in pawns:
        pawns_new = pawns[:]
        pawns_new.remove(p)  # remove the candidate
        secure_pos = board.get_secure_positions()

        for s in secure_pos:
            tx, ty = s
            b = Board(board.sizeX, board.sizeY, board.board)
            if b.is_pawn_threats_others(p, tx, ty) is True:
                continue
            b.set_pawn_in(p, tx, ty)
            findSolutions(b, pawns_new, M, N)

    return board


if __name__ == '__main__':
    main()
