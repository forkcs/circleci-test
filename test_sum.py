import pytest


@pytest.mark.parametrize(
    'a, b, result', [
            (1, 2, 3),
            (2, 1, 3)
        ]        
)
def test_sum_operator(a: int, b: int, result: int):
    assert a + b == result

