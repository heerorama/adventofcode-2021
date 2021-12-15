numbers = [int(line) for line in open('day1.txt', 'r').readlines()]

count = sum(
    numbers[i] > numbers[i - 1]
    for i in range(1, len(numbers))
)
print(f'Part 1: {count}')

count = sum(
    numbers[i] > numbers[i - 3]
    for i in range(3, len(numbers))
)
print(f'Part 2: {count}')