import pytest

import intcode
from intcode import ParameterMode as PM

@pytest.mark.parametrize(
    "param_opcode,expected",
    [
        (2, {'opcode': 2, 'p1': PM(0), 'p2': PM(0), 'p3': PM(0)}),
        (1002, {'opcode': 2, 'p1': PM(0), 'p2': PM(1), 'p3': PM(0)}),
        (1099, {'opcode': 99, 'p1': PM(0), 'p2': PM(1), 'p3': PM(0)}),
        (10199, {'opcode': 99, 'p1': PM(1), 'p2': PM(0), 'p3': PM(1)}),
    ]
)
def test_instruction_decode(param_opcode, expected):
    opcode  = intcode.OpCode(param_opcode)

    assert opcode.opcode == expected["opcode"]
    assert opcode.p1 == expected["p1"]
    assert opcode.p2 == expected["p2"]
    assert opcode.p3 == expected["p3"]

@pytest.mark.parametrize(
    "intput, expected",
    [
        ("1,3,0,3,99", [1,3,0,4,99]),
        ("11101,100,-1,5,99", [11101, 100, -1, 99, 99]),
        ("1101,100,-1,5,99,0", [1101, 100, -1, 5, 99, 99])
    ]
)
def test_addop(intput, expected):
    intput = intcode.Memory(intput)
    output = intcode.compute(intput)
    assert output == expected

@pytest.mark.parametrize(
    "intput, expected",
    [
        ("2,3,0,3,99", [2,3,0,6,99]),
        ("11102,100,-1,5,99", [11102, 100, -1, -100, 99]),
        ("1102,100,-1,5,99,0", [1102, 100, -1, 5, 99, -100])
    ]
)
def test_multop(intput, expected):
    intput = intcode.Memory(intput)
    output = intcode.compute(intput)
    assert output == expected

def test_intputop():
    intput = "3,0,4,0,99"
    expected = [5,0,4,0,99]
    intput = intcode.Memory(intput)
    output = intcode.compute(intput)
    assert output == expected

def test_outputop(capsys):
    intput = "4,2,4,0,99"
    expected = [1,0,4,0,99]
    intput = intcode.Memory(intput)
    output = intcode.compute(intput)
    captured = capsys.readouterr()
    assert captured.out == "4\n4\n"
    # assert output == expected

@pytest.mark.parametrize(
    "intput, expected",
    [
        ("1,1,1,4,99,5,6,0,99", [30,1,1,4,2,5,6,0,99]),
        ("1101,100,-1,4,0", [1101, 100, -1, 4, 99]),
        ("11101,100,-1,4,99", [11101, 100, -1, 99, 99])
    ]
)
def test_whole(intput, expected):
    intput = intcode.Memory(intput)
    output = intcode.compute(intput)
    assert output == expected
    