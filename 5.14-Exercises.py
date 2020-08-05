import time
import turtle



#Ex 1 : time.time()
since = time.time()
days = since // 86400
nsince = since - 86400 * days
hours = nsince // 3600
nsince = (nsince - hours * 3600)
minutes = nsince // 60
nsince = (nsince - minutes * 60)
seconds = nsince 

print(days, hours, minutes, seconds)

#Ex 2 : Fermat
def check_fermat(a,b,c,n):
    if a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

#Ex 3 : Triangle test
def is_triangle(a,b,c):
    if abs(b-c) < a < abs(b+c):
        print("Yes")
    else:
        print("No")

def is_triangle_prompt():
    a = int(input("Enter first edge : "))
    b = int(input("Enter second edge : "))
    c = int(input("Enter third edge : "))
    is_triangle(a,b,c)

is_triangle_prompt()


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob = turtle.Turtle()
bob.speed(0)


#Ex 5 : Koch Curve
def draw_koch(t,x):
    if x < 3:
        t.fd(x)
    else:
        draw_koch(t,x/3)
        t.lt(60)

        draw_koch(t,x/3)
        t.rt(120)

        draw_koch(t,x/3)
        t.lt(60)

        draw_koch(t,x/3)

def snowflake(t,n):
    for i in range(n):
        draw_koch(t, 200)
        t.rt(360/n)

snowflake(bob, 12)

turtle.mainloop()