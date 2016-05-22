import unittest
from friendly_chess.board import Board

# Here's our "unit tests".
class BoardTests(unittest.TestCase):

    def testEmpty(self):
        board = Board(3, 3)
        self.failUnless(board.get_pawn_from(0, 0) == ' ')

    def testSetKnight(self):
        board = Board(3, 3)
        board.set_pawn_in('N', 1, 0)
        self.failUnless(board.get_pawn_from(1, 0) == 'N')
        self.failUnless(board.get_pawn_from(0, 0) == ' ')

def main():
    unittest.main()

if __name__ == '__main__':
    main()