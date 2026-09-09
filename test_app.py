import pytest
from app import find_max, count_evens
@pytest.mark.parametrize("numbers, expected", [([1, 5, 3], 5),2([-10, -2, -7], -2),([4, 4, 4], 4),])

def test_find_max(numbers, expected):
    assert find_max(numbers) == expected
@pytest.mark.parametrize("numbers, expected", [([1, 2, 3, 4], 2),([1, 3, 5], 0),([2, 4, 6, 8], 4),])

def test_count_evens(numbers, expected):
    assert count_evens(numbers) == expected

def test_add():
    assert add(2, 3) == 7

def test_subtract():
    assert subtract(5, 3) == 2

