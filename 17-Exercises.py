
# Ex 1
class Time:
    """Represents the time.

    attributes : seconds
    """
    def __init__(self, hour, minute, second):
        self.second = hour * 3600 + minute * 60 + second
    def __str__(self):
        hour = (self.second // 3600) % 60
        minute = (self.second // 60) % 60
        second = self.second % 60
        return "%.2d:%.2d:%.2d" % (hour, minute, second)


t = Time(1,2,3)
print(t)


# Ex 2
class Kangaroo:
    def __init__(self):
        self.pouch_contents = []
    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
    def __str__(self):
        return self.pouch_contents.__str__()

one = Kangaroo()
two = Kangaroo()
one.put_in_pouch(two)
print(one)