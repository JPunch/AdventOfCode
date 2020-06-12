'''advent of code 2019 day4 first attempt at unit testing'''

import unittest
from day4 import is_password


example1 = 111111
example2 = 223450
example3 = 123789
example4 = 112233
example5 = 123444
example6 = 111122

class IsPasswordTests(unittest.TestCase):
    def test_ex1(self):
        return self.assertEqual(is_password(example1), True)
    def test_ex2(self):
        return self.assertEqual(is_password(example2), False)
    def test_ex3(self):
        return self.assertEqual(is_password(example3), False)


class IsPasswordTests(unittest.TestCase):
    def test_ex1(self):
        return self.assertEqual(is_password(example1), True)
    def test_ex2(self):
        return self.assertEqual(is_password(example2), False)
    def test_ex3(self):
        return self.assertEqual(is_password(example3), False)


if __name__ == "__main__":
    unittest.main()