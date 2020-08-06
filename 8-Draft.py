

def back_str(s):
    if len(s) == 0:
        return
    print(s[-1])
    back_str(s[:-1])

def back_str2(s):
    for letter in s:
        print(letter)

x = "ahmet"

print(x.find("et",1,3))

print("ahmet" in "ahme t can")

def compare_str(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

print(compare_str("Ahmet", "Mehmet"))