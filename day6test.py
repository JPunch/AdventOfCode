'''Advent of code day 6 tests'''
import unittest
from day6 import countorbits
from day6 import tosanta

#example1 = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L"
example1 = [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E'], ['E', 'F'], ['B', 'G'], ['G', 'H'], ['D', 'I'], ['E', 'J'], ['J', 'K'], ['K', 'L']]
example2 = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L K)YOU I)SAN"
example2 = [x.split(")") for x in example2.split()] #had to setup input because bad :)

class CountOrbits(unittest.TestCase):
    def test_ex1(self):
        return self.assertEqual(countorbits(example1)[0], 42)


class ToSanta(unittest.TestCase):
    def test_ex1(self):
        return self.assertEqual(tosanta(example2), 4)


if __name__ == "__main__":
    unittest.main()