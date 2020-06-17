from unittest import TestCase, main
from snake import can_move

class TestCanMove(TestCase):
    def test_cannot(self):
        self.assertEqual(
            can_grow(
              [[1, 1], [2, 1]],
              'R'
            ), False)

    def test_can(self):
        self.assertEqual(
            can_grow(
              [[1, 1], [2, 1]],
              'L'
            ), True)

if __name__ == '__main__':
    main()

