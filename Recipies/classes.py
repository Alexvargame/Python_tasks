import math
import operator
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)
    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)

points=[
Point(2,3),
Point(1,4),
Point(0,2),
Point(1,5)
]
p=Point(5,6)
print(operator.methodcaller('distance',0,0)(p))
for p in points.sort(key=operator.methodcaller('distance',0,0)):
    print(key)
    print(p)
