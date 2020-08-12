import math
import turtle


class Point:
    """Represents a 2-D point."""

class Rectange:
    """Represents a Rectangle.
    attributes : corner, width, height
    """

class Circle:
    """ Represent a circle.
    attributes : center, radius
    """

c = Circle()
c.center = Point()
c.center.x = 150
c.center.y = 100
c.radius = 75


rect = Rectange()
rect.corner = Point()
rect.corner.x = 100
rect.corner.y = 75
rect.width = 100
rect.height = 500

def point_in_circle(circ, p):
    center_distance = math.sqrt((p.x - circ.center.x)**2 + (p.y - circ.center.y)**2)
    return center_distance <= circ.radius

def rect_in_circle(circ, rect):
    p1 = rect.corner
    p2 = Point()
    p2.x = rect.corner.x + rect.width
    p2.y = rect.corner.y
    p3 = Point()
    p3.x = rect.corner.x + rect.width
    p3.y = rect.corner.y + rect.height
    p4 = Point()
    p4.x = rect.corner.x
    p4.y = rect.corner.y + rect.height
    return point_in_circle(circ, p1) and point_in_circle(circ, p2) and point_in_circle(circ, p3) and point_in_circle(circ, p4)

p = Point()
p.x = 200
p.y = 150

print(point_in_circle(c, p))
print(rect_in_circle(c, rect))


t = turtle.Turtle()

def draw_rect(t, rect):
    t.fd(rect.width)
    t.lt(90)

    t.fd(rect.height)
    t.lt(90)

    t.fd(rect.width)
    t.lt(90)

    t.fd(rect.height)


draw_rect(t,rect)
turtle.mainloop()