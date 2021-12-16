#day2 of the advent of code 2021. Python skill test 16-12-2021 Part1 & Part 2

data = open("day2.txt")
#part1
pos = depth = 0
for line in data:
    command, value = line.split()
    value = int(value)
    if command == 'forward':
        pos += value
    elif command == 'down':
        depth += value
    elif command == 'up':
        depth -= value
print('Awnser Part1 ', pos * depth)

#part2
data = open("day2.txt")
pos = depth = aim = 0
for line in data:
    command, value = line.split()
    value = int(value)
    if command == 'forward':
        pos += value
        depth += (aim * value)
    elif command == 'down':
        aim += value
    elif command == 'up':
        aim -= value
print('Awnser Part2 ', pos * depth)
