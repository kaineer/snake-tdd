from unittest import TestCase, main
from snake import move

class TestMove(TestCase):
    def test_move_up(self):
        self.assertEqual(move([5, 5], 'U'), [5, 4])

    def test_move_down(self):
        self.assertEqual(move([5, 5], 'D'), [5, 6])

    def test_move_left(self):
        self.assertEqual(move([5, 5], 'L'), [4, 5])

    def test_move_right(self):
        self.assertEqual(move([5, 5], 'R'), [6, 5])

if __name__ == '__main__':
    main()

