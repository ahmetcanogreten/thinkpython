import turtle
import math
bob = turtle.Turtle()
mike = turtle.Turtle()



def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, length, n, angle):
    """Draws n line segments"""
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, length, n):
    polyline(t, length, n, 360/n)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, step_length, n, step_angle)

circle(bob, 200)
turtle.mainloop()