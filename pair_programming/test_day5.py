import pytest

import intcode
from intcode import ParameterMode as PM

@pytest.mark.parametrize(
    "param_opcode,expected",
    [
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

def test_addop():
    pass
def test_multop():
    pass
def test_inputop():
    pass
def test_outputop():
    pass