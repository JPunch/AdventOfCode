'''Advent of code 2019 day12 tests'''

import unittest
from day14 import fuel_parse, calc_fuel

class FuelAmount(unittest.TestCase):
    def testex1(self):
        example1 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""
        example1 = fuel_parse(example1)
        fuel_amount = calc_fuel(example1)
        return self.assertEqual(fuel_amount, 13312)


if __name__ == "__main__":
    unittest.main()