import string
import random

# Ex 1
def swear():
    w = dict()
    for each in string.punctuation:
        w[ord(each)] = None
    for each in string.whitespace:
        w[ord(each)] = None
    fin = open("13-Ex Line.txt")
    for line in fin:
        word = line.strip().translate(w)
        print(word)

# Ex 2
def analyze_book():
    w = dict()
    for each in string.punctuation:
        w[ord(each)] = None
    for each in string.whitespace:
        w[ord(each)] = None
    
    fin = open("13-Pride.txt")
    words = dict()
    for line in fin:
        t = line.strip().split()
        for word in t:
            tmp = word.translate(w).lower()
            words[tmp] = words.setdefault(tmp, 0) + 1

    for each in words:
        print(each, words[each])
#############

def histogram(t):
    d = dict()
    for each in t:
        d[each] = d.setdefault(each, 0) + 1
    return d

def choose_from_hist(t):
    deck = list()
    for each in t:
        for i in range(t[each]):
            deck.append(each)
    return random.choice(deck)


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line,hist):
    line = line.replace("-", " ")

    for word in line.split():
        word = word.strip(string.whitespace + string.punctuation)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file("13-Pride.txt")

def most_common(h):
    w = []
    for each in h:
        w.append((h[each], each))
    w.sort(reverse=True)
    return w

def print_most_common(hist, num=10):
    t = most_common(hist)
    print("Most common", num, "words are:")
    for i in range(num):
        print(t[i][0], t[i][1], sep="\t")


fin = open("words.txt")
dic = dict()
for line in fin:
    w = line.strip()
    dic[w] = None

def subtract(d1, d2):
    d = dict()
    for key in d1:
        if not key in d2:
            d[key] = None
    return d


s1 = set(hist)
s2 = set(dic)


def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)
    return random.choice(t)


###############################




def create_markov(filename):
    d = dict()
    fp = open(filename)
    prev_word = ""

    for line in fp:
        sentence = line.split()
        if len(sentence):
            if len(prev_word):
                    d[prev_word] = d.get(prev_word, []) + [sentence[0]]

            for i in range(len(sentence)-1):            
                d[sentence[i]] = d.get(sentence[i], []) + [sentence[i+1]]
            prev_word = sentence[len(sentence)-1]
            d[prev_word] = d.get(prev_word, [])
    
    return d

markov = create_markov("13-Pride.txt")

first = random.choice(list(markov.keys()))
print(first, end=" ")

for i in range(100):
    next_word = random.choice(markov[first])
    print(next_word, end=" ")
    first = next_word
print()