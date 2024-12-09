import sys

def validateLevel(levels):
    increasing = levels[0] < levels[1]

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i+1])
        if not (1 <= diff <= 3):
            return False
        elif increasing and levels[i] >= levels[i+1]:
            return False
        elif not increasing and levels[i] <= levels[i+1]:
            return False
    return True

def part1():
    count = 0

    for line in sys.stdin:
        levels = list(map(int, line.split()))
        if validateLevel(levels):
            count += 1
    print(count)

def canDampen(levels):
    increasing = levels[0] < levels[1]
    problems = []

    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i+1])
        if not (1 <= diff <= 3):
            problems.append(i)
        elif increasing and levels[i] >= levels[i+1]:
            problems.append(i)
        elif not increasing and levels[i] <= levels[i+1]:
            problems.append(i)
    
    if len(problems) == 0:
        return True

    # brute force: try every possible removal
    for idx in range(len(levels)):
        # remove problem idx
        newLevels = levels[:idx] + levels[idx+1:]
        if validateLevel(newLevels):
            return True
    return False

def part2():
    count = 0

    for line in sys.stdin:
        levels = list(map(int, line.split()))
        if canDampen(levels):
            count += 1
    print(count)

part2()