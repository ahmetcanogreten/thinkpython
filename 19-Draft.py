import math
from collections import Counter

from collections import namedtuple



x = 19
y = math.log(x) if x > 0 else float("nan")

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

def capitalize_all(t):
    return [s.capitalize() for s in t]

def only_upper(t):
    return [s for s in t if s.isupper()]


g = (x**3 for x in range(100))
for val in g:
    print(val)

print(any(letter == "t" for letter in "monty"))

count = Counter("parrot")
print(count)


Point = namedtuple("Point", ["x", "y"])
p = Point(3,4)

print(p)

def printall(*args):
    print(args)

printall(1,2,3,4,5)

def printall2(*args, **kwargs):
    print(args, kwargs)

printall2(1,2,3,third = "2")

d = dict(x = 1, y = 2)
printall2(**d)