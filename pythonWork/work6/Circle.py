from shape import Point
import math


class Circle:
    def __init__(self, x, y, radius):
        self.p = Point(x, y)
        self.radius = radius
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)
    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)
class Circles(Circle):
    def _area_(self):
        return math.sqrt((3)*(self.radius)^2)
    def _circumference_(self):
        return math.sqrt(3*2*self.radius)


a = Circles(1,2,3)
print(a._area_())
print(a._circumference_())
