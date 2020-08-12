import math
import copy

class Point:
    """Represents a point in 2-D space."""


def print_point(p):
    print("(%g, %g)" % (p.x, p.y))

def distance_between(p1, p2):
    return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

blank = Point()
blank.x = 3.0
blank.y = 4.0

ori = Point()
ori.x = 0
ori.y = 0

class Rectangle:
    """Represent a rectange.

    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect , dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

print(box.width, box.height)
grow_rectangle(box, 100, 100)
print(box.width, box.height)

box_copy = copy.copy(box)
print(box_copy.width, box_copy.height)
print(box.corner == box_copy.corner)

po1 = Point()
po1.x = 0.0
po1.y = 0.0

po2 = copy.copy(po1)
print(po1 == po2)


print(isinstance(po1, Rectangle))
print(hasattr(box, "width"))