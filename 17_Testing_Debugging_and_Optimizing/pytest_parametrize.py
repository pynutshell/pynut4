import pytest

@pytest.mark.parametrize("x,y,expected",
             [
                 (1, 0, True),
                 (0, 1, False)
             ])
def test_is_greater(x, y, expected):
    assert (x > y) == expected

