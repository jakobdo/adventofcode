with open("day1.txt") as f:
        for cnt, line in enumerate(f):
                new_line = line.strip()
                print(f"Line: {cnt} : {new_line}")
