

eng2sp = dict()
eng2sp["one"] = "uno"
eng2sp["two"] = "dos"

eng2sp = {"one" : "uno", "two" : "dos", "three" : "tres"}

values = eng2sp.values()


def histogram(s):
    d = dict()
    for each in s:
        d[each] = d.get(each, 0) + 1
    return d


def reverse_lookup(d, v):
    for each in d:
        if d[each] == v:
            return each
    raise LookupError("value does not appear in the dictionary")


def inverse_dict(d):
    inverse = dict()
    for each in d:
        if d[each] in inverse:
            inverse[d[each]].append(each)
        else:
            inverse[d[each]] = [each]
    return inverse


known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]
    else:
        known[n] = fibonacci(n-1) + fibonacci(n-2)
        return known[n]

def fibonacci_old(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_old(n-1)+fibonacci_old(n-2)

count = 0
def example():
    global count
    count = count + 1

example()
print(count)
