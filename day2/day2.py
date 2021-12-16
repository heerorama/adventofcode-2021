#day2 of the advent of code 2021. Python skill test 16-12-2021 Part1 & Part 2

data = open("day2.txt")
#part1
pos = 0
depth = 0
for line in data:
    command, value = line.split( )
    value = int(value)
    if command == 'forward':
        pos = pos + value
    elif command == 'down':
        depth = depth + value
    elif command == 'up':
        depth = depth - value
print('Awnser Part1 ', pos * depth)

#part2
data = open("day2.txt")
pos = 0
depth = 0
aim = 0
for line in data:
    command, value = line.split( )
    value = int(value)
    if command == 'forward':
        pos = pos + value
        depth = depth + (aim * value)
    elif command == 'down':
        aim = aim + value
    elif command == 'up':
        aim = aim - value
print('Awnser Part2 ', pos * depth)
