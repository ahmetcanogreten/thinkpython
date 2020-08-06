import time

# Ex 1
fin = open("words.txt")
words = []
d = dict()
for each in fin:
    words.append(each.strip())
    d[each] = 1

def binary_search(t, value):
    start = 0
    end = len(t)-1
    while start <= end:
        middle = (start+end) // 2
        if start == end:
            if t[start] == value:
                return start
            else:
                return -1
        if t[middle] == value:
            return middle
        elif t[middle] < value:
            start = middle+1
        else:
            end = middle-1
    return -1


def compare_search():
    binarytime = 0
    for each in words:
        start = time.time()
        binary_search(words, each)
        end = time.time()
        binarytime += end - start
    inlisttime = 0
    for each in words:
        start = time.time()
        each in words
        end = time.time()
        inlisttime += end - start
    indicttime = 0
    for each in words:
        start = time.time()
        each in d
        end = time.time()
        indicttime += end - start

    binarytime = binarytime / len(words)
    inlisttime = inlisttime / len(words)
    indicttime = indicttime / len(words)
    print("binary : {}, list : {}, dict : {}", binarytime, inlisttime, indicttime)

# Ex 2
def invert_dict(d):
    inverse = dict()
    for each in d:
        inverse[d[each]] = inverse.setdefault(d[each], []) + [each]
    return inverse

# Ex 4
def has_duplicates(t):
    d = dict()
    for each in t:
        if each in d:
            return True
        else:
            d[each] = 1
    return False