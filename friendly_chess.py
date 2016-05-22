#!/usr/bin/env python
""" Main script of FriendlyChess. """

from __future__ import print_function
from __future__ import absolute_import
from friendly_chess.board import Board


def main():
    """ Main of the project. """
    print("started")
    board = Board(3, 3)
    print(board)
    print("finished")
    return

if __name__ == '__main__':
    main()
