from collections import namedtuple
from math import sqrt

Point = namedtuple('Point', 'x y')

def diff(a, b):
    return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

a = Point(1, 1)
b = Point(2, 1)
room = Point(3, 2)
def answer(room, a, b):
    print "no deflection", diff(a, b)
    print "one deflection left", diff(a, Point(-1 * b.x, b.y))
    print "one deflection right", diff(a, Point(2 * room.x - b.x, b.y))
    print "one deflection top", diff(a, Point(b.x, 2 * room.y - b.y))
    print "one deflection bottom", diff(a, Point(b.x, -1 * b.y))
    return 0

print answer(room, a, b)

