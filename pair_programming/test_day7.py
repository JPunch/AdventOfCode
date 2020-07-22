import pytest
import pair_programming.intcode


@pytest.mark.parametrize(
    "start_mem, end_mem",
    [
        ()
    ]
)

def test_day7_programs(start_mem, end_mem):
    output = day7(start_mem)
    assert output == end_mem