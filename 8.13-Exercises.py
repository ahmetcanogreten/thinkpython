
# Ex 2
string = "banana"
print(string.count("a"))

# Ex 3
def is_palindrome(s):
    return s == s[::-1]

# Ex 5
def rotate_word(s, amount):
    nstr = ""
    for c in s:
        nstr = nstr + chr(ord(c)+amount)
    return nstr

print(rotate_word("Gur", -13))