import pytest
from programs import string_gen

#check if the output is a string
def test_type():
    assert isinstance(string_gen.string_gen(),str) == True 

#check if the output is 5 character long
def test_length():
    assert len(string_gen.string_gen()) == 5

#check if the output is lower case
def test_lower_case():
    assert islower(string_gen.string_gen()) == True