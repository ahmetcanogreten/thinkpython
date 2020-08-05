

#Ex 1 : Ackermann function
def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

print(ack(3,4))

# Ex 2 : Palindrome

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    if len(s) == 0:
        return True
    return first(s) == last(s) and is_palindrome(middle(s))


print(is_palindrome(""))

# Ex 3 : Power

def is_power(a,b):
    if a == 1:
        return True
    return a % b == 0 and is_power(a/b,b) 

print(is_power(1,2))