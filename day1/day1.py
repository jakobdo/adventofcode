import os
basedir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(basedir, "day1.txt")
numbers = []
with open(filename) as f:
    for cnt, line in enumerate(f):
        numbers.append(int(line.strip()))
print(sum(numbers))


def compute(numbers):
    val = 0
    seen = {val}

    length = len(numbers)
    while True:
        for x in range(length):
            val += numbers[x]
            if val in seen:
                return val
            else:
                seen.add(val)


print(compute(numbers))
