'''Tests for Advent of code 2019 day16 using pytest'''

import pytest
import day16

@pytest.mark.parametrize(
    "signal, fitted_pattern",
    [
        ([1,1,1,1,1,1], [0,1,0,-1,0,1]),
        ([1,1,1,1,1,1,1,1,1,1,1,1], [0,1,0,-1,0,1,0,-1,0,1,0,-1])
    ]
)
def test_fit_to_signal(signal, fitted_pattern):
    pattern = day16.Pattern("0,1,0,-1")
    pattern.fit_to_signal(signal)
    assert pattern.fitted_pattern == fitted_pattern