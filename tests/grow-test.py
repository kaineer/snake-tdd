from unittest import TestCase, main
from snake import grow

class TestGrow(TestCase):
    def test_grow_up(self):
        self.assertEqual(grow([[2, 2]], 'U'), [[2, 1], [2, 2]])

    def test_grow_down(self):
        self.assertEqual(grow([[2, 2]], 'D'), [[2, 3], [2, 2]])

    def test_grow_right(self):
        self.assertEqual(grow([[2, 2]], 'R'), [[3, 2], [2, 2]])

    def test_grow_left(self):
        self.assertEqual(grow([[2, 2]], 'L'), [[1, 2], [2, 2]])

if __name__ == '__main__':
    main()
