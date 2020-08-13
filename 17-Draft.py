

class Time:
    """

    attributes : hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return "%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second)
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    def __radd__(self, other):
        return self.__add__(other)
    
    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))
    def time_to_second(self):
        return self.hour * 3600 + self.minute * 60 + self.second
    def is_after(self, other):
        return self.time_to_second() > other.time_to_second()
    def add_time(self, other):
        seconds = self.time_to_second() + other.time_to_second()
        return second_to_time(seconds)
    def increment(self, seconds):
        seconds += self.time_to_second()
        return second_to_time(seconds)
    
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)
    def __add__(self, other):
        p = Point(self.x + other.x, self.y + other.y)
        return p

def second_to_time(s):
    t = Time()
    t.hour = (s // 3600) % 60
    t.minute = ((s - t.hour * 3600) // 60) % 60
    t.second = (s - t.hour * 3600 - t.minute * 60) % 60
    return t


t = Time()
t.hour = 1
t.minute = 2
t.second = 3
t.print_time()
end = t.increment(645)
end.print_time()

default = Time()
default.print_time()

p = Point(3,4)
print(p.x, p.y)
print(default)
print(p)
print(t+default)

p1 = Point(3,4)
p2 = Point(7,9)
print(p1+p2)