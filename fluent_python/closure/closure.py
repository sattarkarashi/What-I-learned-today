## Closures

class Averager():
    def __init__(self):
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)

        return sum(self.series)/len(self.series)

avg = Averager()

print(avg(6))
print(avg(8))


def make_average():
    series = []

    def averager(new_value):
        print(series)

        series.append(new_value)

        return sum(series)/len(series)
    
    return averager

avg = make_average()

print(avg(6))
print(avg(8))


# Using nonlocal variables to refactor the above code
def make_average_nonlocal():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total

        count += 1
        total += new_value

        return total/count
    
    return averager
    
avg = make_average_nonlocal()

print(avg(6))
print(avg(8))