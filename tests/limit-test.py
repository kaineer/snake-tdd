from unittest import TestCase, main
from snake import limit

class TestLimit(TestCase):
    def test_limit_overflow(self):
        self.assertEqual(limit([1, 2, 3, 4, 5], 4), [1, 2, 3, 4])

    def test_limit_short(self):
        self.assertEqual(limit([1, 2, 3], 4), [1, 2, 3])

    def test_limit_equal(self):
        self.assertEqual(limit([1, 2, 3, 4], 4), [1, 2, 3, 4])

if __name__ == '__main__':
    main()
