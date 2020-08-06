import random

# Ex 1
def nested_sum(t):
    sum = 0
    for i in t:
        for j in i:
            sum+=j
    return sum

# Ex 2
def cumsum(t):
    newt = [t[0]]
    for i in range(1,len(t)):
        newt.append(newt[i-1]+t[i])
    return newt

# Ex 3
def middle(t):
    return t[1:-1]

# Ex 4
def chop(t):
    t.pop(0)
    t.pop(-1)
# Ex 5
def is_sorted(t):
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True
# Ex 6
def is_anagram(t1,t2):
    if not len(t1) == len(t2):
        return False
    t1 = t1[:]
    t2 = t2[:]
    for i in range(len(t1)):
        if t1[i] in t2:
            t2.remove(t1[i])
        else:
            return False
    return True

#Ex 7
def has_duplicates(t):
    for i in range(len(t)-1):
        if t[i] in t[:i]+t[i+1:]:
            return True
    return False

# Ex 8
def bday():
    bdays = []
    for i in range(23):
        bdays.append(random.randint(1,365))
    return has_duplicates(bdays)

def bday_prob():
    max = 1000
    satis = 0
    for i in range(max):
        if bday():
            satis+=1
    return satis/max

# Ex 9
t = []
def append_word():
    fin = open("words.txt")
    for each in fin:
        word = each.strip()
        t.append(word)
    print("Done append")



def plus_word():
    t = []
    fin = open("words.txt")
    for each in fin:
        word = each.strip()
        t = t + [word]
    print("Done plus")

# Ex 10
def in_bisect(sorted, value):
    start = 0
    end = len(sorted)-1
    while start < end:
        middle = (end+start)//2
        if sorted[middle] == value:
            return True
        elif sorted[middle] < value:
            start = middle+1
        else:
            end = middle-1
    return False

# Ex 11
def reverse_pair(sorted):
    for each in sorted:
        if in_bisect(sorted, each[::-1]):
            print(each,each[::-1])


# Ex 12
def interlock(t):
    nword = ""
    for i in range(len(t)-1):
        for j in range(i, len(t)):
            if len(t[i]) == len(t[j]):
                for k in range(len(t[i])):
                    nword = nword + t[i][k] + t[j][k]
                if in_bisect(t, nword):
                    print(t[i],t[j], nword)
                nword = ""



