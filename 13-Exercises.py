import string
import math
import matplotlib.pyplot as plt


fin = open("13-Pride.txt")
d = dict()
for line in fin:
    words = line.split()
    for each in words:
        word = each.strip(string.punctuation + string.whitespace)
        d[word] = d.get(word, 0) + 1

freq_d = dict()
for key in d:
    freq_d[d[key]] = freq_d.get(d[key], []) + [key]


t = []
for key in freq_d:
    t.append((key, freq_d[key]))
t.sort(reverse=True)

logf = []
for freq,wordlist in t:
    logf.append(math.log(freq))


plt.plot(logf)
plt.ylabel('Frequency')
plt.show()