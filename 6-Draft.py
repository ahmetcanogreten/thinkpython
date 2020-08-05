import math


e = math.exp(1)


def area(radius):
    return 2 * math.pi * radius

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

def compare(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def fac(n):
    if not isinstance(n,int):
        print("Fac is only def for int")
        return None
    if n <= 0:
        return 1
    else:
        return n * fac(n-1)

print(fac(5.1))
