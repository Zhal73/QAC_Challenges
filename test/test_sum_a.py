import pytest
from programs.sum_digit import sum_a

def test_one():
    for b in range(10):
        assert sum_a(b) == b + int(str(b)+str(b)) + int(str(b)+str(b)+str(b)) + int(str(b)+str(b)+str(b)+str(b))