import os


def sed(pat, rep, file1, file2):
    try:
        f1 = open(file1, "r")
    except:
        print("The file doesn't exist...")
    
    try:
        f2 = open(file2, "w")
    except:
        print("Something happened while creating new file...")
    
    for line in f1:
        f2.write(line.replace(pat, rep))

    f1.close()
    f2.close()

def main():
    sed("will be", "was", "from.txt", "to.txt")


t = []

def find_files(ext, path):
    for each in os.listdir(path):
        npath = os.path.join(path,each)
        if os.path.isdir(npath):
            find_files(ext, npath)
        else:
            if ext in each:
                t.append(npath)

            



if __name__ == "__main__":
    main()
    find_files(".mp3", "/home/jng/Documents/Repo/thinkpython/mp3")


