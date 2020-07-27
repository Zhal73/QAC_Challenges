import pytest
from programs.sevenNotFive import sevenNotFive

def test_sevenNotFive():
    for string in sevenNotFive():
        assert "2100" not in string