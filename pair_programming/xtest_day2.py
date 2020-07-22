'''Advent of code 2019 day2 collaboration with https://github.com/LiamLombard'''
import pytest

import pair_programming.intcode

@pytest.mark.parametrize(
    "start_mem,end_mem",
    [
        ("1,0,0,0,99", [2,0,0,0,99]),
        ("2,3,0,3,99", [2,3,0,6,99]),
        ("2,4,4,5,99,0", [2,4,4,5,99,9801]),
        ("1,1,1,4,99,5,6,0,99", [30,1,1,4,2,5,6,0,99])
    ]
)
def test_day2_programs(start_mem, end_mem):
    mem = intcode.Memory(start_mem)
    output = intcode.compute(mem)
    assert output == end_mem
    

@pytest.mark.parametrize(
    "input, parse_input",
    [
        ("1,0,0,0,99", [1,0,0,0,99]),
        ("1,1,0,0,99", [1,1,0,0,99]),
        ("2,4,4,5,99,0", [2,4,4,5,99,0]),
        ("1,1,1,4,99,5,6,0,99", [1,1,1,4,99,5,6,0,99])
    ]
)
def test_day2_parse(input, parse_input):
    output = intcode.parse_string(input)
    assert output == parse_input

@pytest.mark.parametrize(
    "input, parse_input",
    [
        ("1,0,0,0,99", 1),
        ("1,1,0,0,99", 1),
        ("2,4,4,5,99,0", 2),
        ("1,1,1,4,99,5,6,0,99", 1)
    ]
)
def test_day2_next_command(input, parse_input):
    memory = intcode.Memory(input)
    output = memory.next_command()
    assert output == parse_input

@pytest.mark.parametrize(
    "input, parse_input",
    [
        ("1,0,0,0,99", [0,0,0]),
        ("1,1,0,0,99", [1,0,0]),
        ("2,4,4,5,99,0", [4,4,5]),
        ("1,1,1,4,99,5,6,0,99", [1,1,4])
    ]
)
def test_day2_get_count_after_pc(input, parse_input):
    memory = intcode.Memory(input)
    output = memory.get_count_after_pc(3)
    assert output == parse_input