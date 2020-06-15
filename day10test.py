'''Advent of code day10 tests'''

import unittest
from day10 import station_location

example1 = "......#.#./#..#.#..../..#######./.#.#.###../.#..#...../..#....#.#/#..#....#./.##.#..###/##...#..#./.#....####"
example2 = "#.#...#.#./.###....#./.#....#.../##.#.#.#.#/....#.#.#./.##..###.#/..#...##../..##....##/......#.../.####.###."
example3 = ".#..#..###/####.###.#/....###.#./..###.##.#/##.##.#.#./....###..#/..#.#..#.#/#..#.#.###/.##...##.#/.....#.#.."

class StationLocationTests(unittest.TestCase):
    def test_ex1(self):
        return self.assertEqual(station_location(example1.split("/")), 33)

    def test_ex2(self):
        return self.assertEqual(station_location(example2.split("/")), 35)

    def test_ex3(self):
        return self.assertEqual(station_location(example3.split("/")), 41)

if __name__ == "__main__":
    unittest.main()