

#Ex 1
def right_justify(s):
    print((70-len(s))*" " + s)

right_justify("aghhhhhmet")

#Ex 2
def do_twice(f, para):
    f(para)
    f(para)

def print_twice(para):
    print(para)
    print(para)

do_twice(print_twice, "spam")

def do_four(f, para):
    do_twice(f, para)
    do_twice(f, para)

do_four(print_twice, "spam")

#Ex 3

def draw_grid():
    print("+", "- " * 4, "+", "- " * 4, "+")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("+", "- " * 4, "+", "- " * 4, "+")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("|", " " * 8, "|", " " * 8, "|")
    print("+", "- " * 4, "+", "- " * 4, "+")

draw_grid()