#day2 of the advent of code 2021. Python skill test 16-12-2021 Part1 & Part 2

def challenge2(data, version):
    pos = depth = aim = 0
    for line in data:
        command, value = line.split()
        value = int(value)     
        if command == 'forward' and version == 'a':
            pos += value
        elif command == 'forward' and version == 'b':
            pos += value
            depth += (aim * value)
        elif command == 'down' and version == 'a':
            depth += value
        elif command == 'down' and version == 'b':
            aim += value
        elif command == 'up' and version == 'a':
            depth -= value
        elif command == 'up' and version == 'b':
            aim -= value
    return(pos * depth)

#data = open("day2.txt")
def feedChallenge2(fileName, version):
    with open(fileName) as data:
        return challenge2(data, version)
