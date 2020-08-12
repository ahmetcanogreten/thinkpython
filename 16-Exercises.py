

class Time:
    """Represents time

    attributes : hour, minute, second
    """

def time_to_second(t):
    return t.hour * 3600 + t.minute * 60 + t.second

def second_to_time(s):
    t = Time()
    t.hour = (s // 3600) % 24
    t.minute = ((s - t.hour * 60) // 60) % 60
    t.second = (s - t.minute * 60 - t.hour * 3600) % 60

    return t

def mul_time(t, n):
    return second_to_time(time_to_second(t) * n)

def print_time(t):
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))

t = Time()
t.hour = 5
t.minute = 12
t.second = 54

print_time(mul_time(t, 154))

def find_pace(time, dis):
    return mul_time(time, 1/dis)


print_time(find_pace(t, 100))