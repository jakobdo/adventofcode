import os


def compute():
    basedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(basedir, "day2.txt")

    with open(filename) as f:
        twos = 0
        threes = 0
        for cnt, line in enumerate(f):
            characters = {}
            for character in line.strip():
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1

            count2 = 0
            count3 = 0

            for character, counts in characters.items():
                if counts == 2:
                    print(f"2 : {character}")
                    count2 += 1
                elif counts == 3:
                    print(f"3 : {character}")
                    count3 += 1

            if count2 > 0:
                twos += 1
            if count3 > 0:
                threes += 1

        print(twos * threes)

def compare_string(s1, s2):
    matches = 0
    for key, c in enumerate(s1):
        if c == s2[key]:
            matches += 1
    return matches

def remove_diff(s1, s2):
    new_str = []
    for key, c in enumerate(s1):
        if c == s2[key]:
            new_str.append(c)
    return "".join(new_str)

def compute_part2():
    basedir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(basedir, "day2.txt")

    lines = []
    best_match = 0
    matches = []

    with open(filename) as f:
        for cnt, line in enumerate(f):
            lines.append(line.strip())

    for x in range(len(lines)):
        for y in range(x+1, len(lines)):
            result = compare_string(lines[x], lines[y])

            if result > best_match:
                best_match = result
                matches = [lines[x], lines[y]]

    print(remove_diff(matches[0], matches[1]))
compute_part2()

