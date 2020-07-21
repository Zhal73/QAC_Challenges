import pytest
from programs.rectangles import rectangle

def test_area():
    for x in range (1,10):
        for y in range (1,10):
            rec=rectangle(x,y)
            assert rec.area() == x*y