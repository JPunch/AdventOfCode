'''Advent of code day10 tests'''

import unittest
from day10 import station_location
from day10 import asteroid_bet

example1 = "......#.#./#..#.#..../..#######./.#.#.###../.#..#...../..#....#.#/#..#....#./.##.#..###/##...#..#./.#....####"
example2 = "#.#...#.#./.###....#./.#....#.../##.#.#.#.#/....#.#.#./.##..###.#/..#...##../..##....##/......#.../.####.###."
example3 = ".#..#..###/####.###.#/....###.#./..###.##.#/##.##.#.#./....###..#/..#.#..#.#/#..#.#.###/.##...##.#/.....#.#.."
example4 = ".#..##.###...#######/##.############..##./.#.######.########.#/.###.#######.####.#./#####.##.#.##.###.##/..#####..#.#########/####################/#.####....###.#.#.##/##.#################/#####.##.###..####../..######..##.#######/####.##.####...##..#/.#####..#.######.###/##...#.##########.../#.##########.#######/.####.#.###.###.#.##/....##.##.###..#####/.#.#.###########.###/#.#.#.#####.####.###/###.##.####.##.#..##"
class StationLocationTests(unittest.TestCase):
    def test_ex1(self):
        return self.assertEqual(station_location(example1.split("/"))[0], 33)

    def test_ex2(self):
        return self.assertEqual(station_location(example2.split("/"))[0], 35)

    def test_ex3(self):
        return self.assertEqual(station_location(example3.split("/"))[0], 41)


class AsteroidBetTests(unittest.TestCase):
    def test_ex1(self):
        return self.assertEqual(asteroid_bet(example4), 802)


if __name__ == "__main__":
    unittest.main()