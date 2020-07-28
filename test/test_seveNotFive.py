import pytest
from programs.sevenNotFive import sevenNotFive

def test_sevenNotFive_one():
        assert "2100" not in sevenNotFive()

def test_sevenNotFive_two():
        assert "2401" in sevenNotFive()
     