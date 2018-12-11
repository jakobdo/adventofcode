start = 0
with open("day1.txt") as f:
        for cnt, line in enumerate(f):
                start += int(line.strip())
print(start)
