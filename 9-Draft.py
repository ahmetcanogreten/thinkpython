

fin = open("words.txt")

# Ex 1
def print_more_20():
    for line in fin:
        word = line.strip()
        if(len(word) > 20):
            print(word)

# Ex 2
def has_no_e(word):
    for c in word:
        if c == "e":
            return False
    return True

def print_no_e_words():
    for line in fin:
        word = line.strip()
        if not ("e" in word):
            print(word)
def calculate_perc_no_e():
    wcount = 0
    ecount = 0
    for line in fin:
        wcount = wcount + 1
        word = line.strip()
        if not ("e" in word):
            ecount = ecount + 1
    return ecount/wcount*100


# Ex 3
def avoids(word, s):
    for c in s:
        if c in word:
            return False
    return True

# Ex 4
def uses_only(word, s):
    for c in word:
        if not (c in s):
            return False
    return True

# Ex 5
def uses_all(word, s):
    for c in word:
        if not (c in s):
            return False
    for c2 in s:
        if not (c2 in word):
            return False
    return True
    return uses_only(s, word)

#Ex 6
def is_abecedarian(word):
    word2 = word.upper()
    for i in range(len(word2)-1):
        if word2[i] > word2[i+1]:
            return False
    return True

