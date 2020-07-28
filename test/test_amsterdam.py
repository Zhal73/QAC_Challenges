import pytest
from programs.amsterdam import name
import random

def test_one():
    assert name("I am hungry, I am going to eat an ham sandwich") == 2

def test_two():
    assert name("Hamburger are not healthy") == 0

def test_three():
    list_one = ("Amsterdam", "car", "ham", "Jupite", "monkey")
    list_two = ("have","jumps", "am",  "drives", "barfs") 
    list_three = ("crazily", "dutifully", "amortization", "merrily", "occasionally.")
    list_four = ("adorable", "shameful", "dirty", "odd", "decontaminator")
    num = random.randrange(0,5)
    
    if num == 2:
        assert name(list_one[num] + ' ' +list_two[num] + ' ' + list_three[num] + ' ' + list_four[num]) == 1
    else:
        assert name(list_one[num] + ' ' +list_two[num] + ' ' + list_three[num] + ' ' + list_four[num]) == 0
