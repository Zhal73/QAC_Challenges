import pytest
from programs.sort_string import sort_string

def test_one():
    assert sort_string("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"

def  test_two():
    assert sort_string("This is a string without duplicates") == "a duplicates is string this without"

def test_three():
    assert sort_string("duplicates duplicates and duplicates this sentence is one sentence full of duplicates") == "and duplicates full is of one sentence this"