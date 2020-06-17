#
from unittest import TestCase, main
from snake import move

class TestFunction(TestCase):
    def test_function(self):
        self.assertEqual(callable(move), True)

if __name__ == '__main__':
    main()
