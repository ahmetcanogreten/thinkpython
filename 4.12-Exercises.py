import turtle
import math

bob = turtle.Turtle()

#Ex 1 : Drawing Flowers
def draw_returning_arc(n, length, angle):
    for i in range(n):
        bob.fd(length)
        bob.lt(angle)
    bob.lt(180-angle*n)
    for j in range(n):
        bob.fd(length)
        bob.lt(angle)
    bob.rt(angle)

def draw_flower(leaf, width, resolution):
    alfa = (width)/(resolution-1)
    theta = 180-alfa-resolution
    for i in range(leaf):
        draw_returning_arc(resolution, 20, alfa)
        bob.lt(180+360/resolution-(180-alfa-theta))

#draw_flower(100,50,10)

#Ex 2 : Drawing Shapes

def draw_shape(t, n, length):
    alfa = 360/n
    theta = (180-alfa)/2
    for i in range(n):
        t.fd((length)/(math.sqrt(2*(1-math.cos(alfa/180*math.pi)))))
        t.lt(180-theta)

        t.fd(length)
        t.lt(180-theta)

        t.fd((length)/(math.sqrt(2*(1-math.cos(alfa/180*math.pi)))))
        t.lt(180)

draw_shape(bob, 20, 50)


turtle.mainloop()