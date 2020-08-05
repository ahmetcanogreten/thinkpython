x = 11

if x > 10:
    print("x is positive")
if x < 10:
    pass # TODO:





if x < 1:
    print("x is less than 1")
elif x < 4:
    print("x is less than 4")
else:
    print("None of them above")


z = 5
if 0 < z < 10:
    print("WTF")


def countdown(n):
    if n <= 0:
        print("Boooom")
    else:
        print(n)
        countdown(n-1)

    
countdown(10)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n("Ahmet", 3)

def recurse():
    recurse()


text = input("What is your name?\n")
print(text)