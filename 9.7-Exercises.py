
# Ex 7
def cartalk_helper(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if len(word) > i+3 and word[i+2] == word[i+3]:
                if len(word) > i+5 and word[i+4] == word[i+5]:
                    return True
    return False

def cartalk():
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if cartalk_helper(word):
            print(word)

# Ex 8
def cartalk2():
    for i in range(100000,1000000):
        if str(i)[2:] == str(i)[2:][::-1]:
            if str(i+1)[1:] == str(i+1)[1:][::-1]:
                if str(i+2)[1:-1] == str(i+2)[1:-1][::-1]:
                    if str(i+3) == str(i+3)[::-1]:
                        print(i)
    
# Ex 9
def mom_daughter():
    count = 0
    while True:
        for g in range(10,99):
            now = 0
            m = int(str(g)[::-1])
            while m > g and m < 100:
                if(g == int(str(m)[::-1])):
                    count+=1
                if count == 6:
                    now = g
                m+=1
                g+=1
            if(count == 8):
                return now

print(mom_daughter())
