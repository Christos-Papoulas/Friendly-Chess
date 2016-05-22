import unittest
from friendly_chess.board import Board
import chess

# Here's our "unit tests".
class Board_Tests(unittest.TestCase):

    def testEmpty(self):
        board = Board(3, 3)
        self.failUnless(board.get_pawn_from(0, 0) == ' ')

    def testSetKnight(self):
        board = Board(3, 3)
        board.set_pawn_in('N', 1, 0)
        self.failUnless(board.get_pawn_from(1, 0) == 'N')
        self.failUnless(board.get_pawn_from(0, 0) == ' ')

class find_solutions_tests(unittest.TestCase):
    def test_find_solutions(self):
        board = Board(3, 3)
        M = 3
        N = 3
        pawns = ['K', 'K', 'R']
        solutions = []
        self.assertRaises(Exception, chess.find_solutions(
            board, pawns, M, N, solutions, 0))
        self.assertNotEqual(len(solutions), 0)

    def test_find_solutions_for4N2R(self):
        M = 4
        N = 4
        pawns = ['N', 'N', 'N', 'N', 'R', 'R']
        board = Board(4, 4)
        solutions = []
        self.assertRaises(Exception, chess.find_solutions(
            board, pawns, M, N, solutions, 0))
        self.assertNotEqual(len(solutions), 0)

def main():
    unittest.main()

if __name__ == '__main__':
    main()