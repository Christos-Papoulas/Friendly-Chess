import unittest
from friendly_chess.board import Board
import chess
from friendly_chess.pawn import King, Queen, Bishop, Knight, Rook


# Here's our "unit tests".
class Board_Tests(unittest.TestCase):

    def testEmpty(self):
        board = Board(3)
        self.failUnless(board.get_pawn_from(0, 0) == ' ')

    def testSetKnight(self):
        board = Board(3)
        board.set_pawn_in(Knight(), 1, 0)
        self.failUnless(board.get_pawn_from(1, 0) == Knight())
        self.failUnless(board.get_pawn_from(0, 0) == ' ')


class find_solutions_tests(unittest.TestCase):
    def test_find_solutions(self):
        board = Board(3)
        pieces = [King(), King(), Rook()]
        solutions = []
        self.assertRaises(Exception, chess.find_solutions(
            board, pieces, solutions))
        self.assertEqual(len(solutions), 4)

        chess.print_solutions(solutions)

    def test_find_solutions_for4N2R(self):
        pieces = [Queen(), Queen(), Queen(), Queen()]
        board = Board(4)
        solutions = []
        self.assertRaises(Exception, chess.find_solutions(
            board, pieces, solutions))
        self.assertEqual(len(solutions), 2)
        chess.print_solutions(solutions)

class is_already_tried_test(unittest.TestCase):
    def test_equal(self):
        board1 = Board(3)
        board1.set_pawn_in(Knight(), 1, 0)
        board2 = Board(3)
        board2.set_pawn_in(Knight(), 1, 0)

        self.assertEqual(board1, board2)
        self.assertEqual(
            board1.board, board2.board)
        board2.set_pawn_in(Knight(), 2, 0)
        self.assertNotEqual(
            board1.board, board2.board)


class check_threads(unittest.TestCase):
    def test_simple(self):
        board1 = Board(3)
        board1.set_pawn_in(Rook(), 0, 0)
        board1.calculate_threats()
        self.assertEqual(
            board1.get_pawn_from(1, 0), 'T')
        self.assertEqual(
            board1.get_pawn_from(2, 0), 'T')
        self.assertEqual(
            board1.get_pawn_from(0, 1), 'T')
        self.assertEqual(
            board1.get_pawn_from(0, 2), 'T')

class equality_checks(unittest.TestCase):
    def test_equal(self):
        king1 = King()
        king2 = King()
        knight = Knight()
        self.assertEqual(king1, king2)
        self.assertNotEqual(knight, king1)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
