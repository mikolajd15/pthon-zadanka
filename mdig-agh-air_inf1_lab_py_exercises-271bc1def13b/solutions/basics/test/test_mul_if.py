import unittest

from basics import mul_if


class TestMultiplyIf(unittest.TestCase):
    def test_predicates(self):
        self.assertEqual(6, mul_if([2, 3, 4], lambda x: x < 4))


if __name__ == '__main__':
    unittest.main()
