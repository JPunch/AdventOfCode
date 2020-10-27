'''Advent of code 2019 day12 tests'''

import unittest
from day14 import fuel_parse, calc_fuel

class Day18P1(unittest.TestCase):
    def testex1(self):
        example1 = """
########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################
"""
        example1 = fuel_parse(example1)
        fuel_amount = calc_fuel(example1)
        return self.assertEqual(fuel_amount, 13312)


if __name__ == "__main__":
    unittest.main()