#day 1 of the advent of code in Python. Just to update the python skills.



def challenge1a(numbers):
    count = sum(
        numbers[i] > numbers[i - 1]
        for i in range(1, len(numbers))
    )
    return count

def challenge1b(numbers):
    count = sum(
        numbers[i] > numbers[i - 3]
        for i in range(3, len(numbers))
    )
    return count

def feedChallenge1a(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
        numbers = [int(line) for line in lines]
        return challenge1a(numbers)

def feedChallenge1b(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
        numbers = [int(line) for line in lines]
        return challenge1b(numbers)




