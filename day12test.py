'''Advent of code 2019 day12 tests'''

import unittest
from day12 import moon_parse, moon_energy, match_state

class MoonEnergy(unittest.TestCase):
    def testex1(self):
        example1 = "<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>"
        moons = moon_parse(example1)
        energy = moon_energy(moons, 100)
        return self.assertEqual(energy, 1940)

class MatchState(unittest):
    def textex1(self):
        example1 = "<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>"
        moons = moon_parse(example1)
        steps = match_state(moons)
        return self.assertEqual(steps, 2772)

if __name__ == "__main__":
    unittest.main()