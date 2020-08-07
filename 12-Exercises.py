

#Ex 1
def most_frequent(s):
    h = dict()
    for each in s:
        h[each] = h.setdefault(each,0) + 1
    inverse = dict()
    for each in h:
        inverse[h[each]] = inverse.setdefault(h[each], []) + [each]
    
    for each in reversed(sorted(inverse)):
        print(each, inverse[each])

#Ex 2

def find_anagrams(n):
    fin = open("words.txt")
    w = dict()
    for each in fin:
        t = list()
        word = each.strip()
        for letter in word:        
            t.append(letter)
        w[tuple(sorted(t))] = w.setdefault(tuple(sorted(t)), []) + [word]

    for pairs in w:
        if len(w[pairs]) == n:
            print(w[pairs])


find_anagrams(11)