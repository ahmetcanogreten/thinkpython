import os
import dbm
import pickle
import shelve # pickle + dbm
import wc

fout = open("output.txt", "w")

line1 = "This here's the wattle,\n"
fout.write(line1)

x = 52
fout.write("In %d years I have spotted %g %s." % (3, 0.1, "camels"))

fout.close()

def os_practice():
    cwd = os.getcwd()
    print(cwd)

    path = os.path.abspath("output.txt")
    print(path)

    print(os.path.exists("output.txt"))
    print(os.path.isdir("output.txt"))

    print(os.path.isdir("/home"))

    print(os.listdir(cwd))


def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


try:
    fin = open("nofile.txt")
except:
    pass

db = dbm.open("captions", "c")
#db["cleese.png"] = "Photo of John Cleese"
#print(db["cleese.png"])



db.close()

t1 = [1,2,3]
s = pickle.dumps(t1)
#print(s)
t2 = pickle.loads(s)
#print(t2)

cmd = "ls -l"
fp = os.popen(cmd)
print(fp.read())
fp.close()

filename = "words.txt"
cmd = "md5sum " + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)

print(wc.linecount("14-Draft.py"))

n = "Ahmet Can Ogreten  "
print(repr(n))