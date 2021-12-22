from __future__ import annotations
import collections

#input of the test
INPUT_S = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''

def counts_position_of_one(lines):
    counts: dict[int, int] = collections.defaultdict(int)

    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                counts[i] += 1
    
    return counts

def generate_new_binary_code(lines):
    num1 = []
    num2 = []

    counts = counts_position_of_one(lines)

    for i in range(len(lines[0])):
        if counts[i] > len(lines) / 2:
            num1.append('1')
            num2.append('0')
        else:
            num1.append('0')
            num2.append('1')

    gamma_rate = int("".join(num1), 2)
    epsilon_rate = int("".join(num2), 2)

    return(gamma_rate * epsilon_rate)


