#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(c1,c2):
    # c1 is a list with 2 values, c1[0] and c1[1]
    return math.sqrt((c2[0] - c1[0])**2 + (c2[1] - c1[1])**2)


if __name__ == "__main__":
    d = distance( (2,4) , (6,3) )
    assert round(d,3) == 4.123
    d = distance( (-3,2.2) , (1,2))
    assert round(d,3) == 4.005


