

t = divmod(456,7)

quotion, remainder = t

def min_max(t):
    return (min(t), max(t))


def sum_all(*args):
    s = 0
    for i in range(len(args)):
        s += args[i]
    return s


def has_match(t1, t2):
    for x, y in zip(t1,t2):
        if x == y:
            return True
    return False

# zip : return list of tuple
d = dict()
d["ogreten", "ahmet"] = 5432180019
print(zip("abc"),"123")