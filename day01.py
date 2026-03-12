import sys


def get_secret_number(directions):
    current = 50
    secret_number = 0

    for d in directions:
        if d[0] == 'L':
            next_number = (current - d[1])
        else:
            next_number = (current + d[1])

        if next_number == 0 and current != 0:
            secret_number += 1
        elif next_number < 0 and current != 0:
            secret_number += 1 + (abs(next_number) // 100)
        elif next_number < 0 and current == 0:
            secret_number += abs(next_number) // 100
        elif next_number > 99:
            secret_number += (next_number // 100)

        current = next_number % 100

    return secret_number


with open(sys.argv[1]) as f:
    lines = f.readlines()
    directions = [(l[0], int(l[1:])) for l in lines]

    print(get_secret_number(directions))
