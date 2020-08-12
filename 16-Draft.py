

class Time:
    """Represents the time of day.

    attributes : hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 29

def print_time(t):
    print("%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second))

def is_after(t1, t2):
    diff = (t1.hour-t2.hour)*60*60 + (t1.minute-t2.minute)*60 + (t1.second-t2.second)
    return diff > 0

def add_time(t1, t2):
    s1 = time_to_second(t1)
    s2 = time_to_second(t2)
    return second_to_time(s1+s2)


def increment(t, seconds):
    t.second += seconds

    ex_minute = t.second // 60
    t.minute += ex_minute
    t.second -= ex_minute * 60

    ex_hour = t.minute // 60
    t.hour += ex_hour
    t.minute -= ex_hour * 60

    t.hour = t % 24

def time_to_second(t):
    return t.hour * 60 * 60 + t.minute * 60 + t.second

def second_to_time(s):
    t = Time()
    t.hour = s // 3600
    t.minute = (s - t.hour * 3600) // 60
    t.second = s - t.hour * 3600 - t.minute * 60
    return t 



print_time(time)
print(is_after(time2, time))
print_time(add_time(time, time2))