import re


def parse_input(path):
    with open(path) as f:
        line = f.readline().strip()
        shapes = []

        while re.match(r'\d+:', line):
            shapes.append(parse_shape(f))
            f.readline()
            line = f.readline()

        tree = []
        while line:
            values = line.split(' ')

            width = int(values[0].split('x')[0])
            height = int(values[0][:-1].split('x')[1])
            amount = [int(val) for val in values[1:]]

            tree.append((width, height, amount))

            line = f.readline()

        return shapes, tree


def parse_shape(f):
    return [
        f.readline().strip(),
        f.readline().strip(),
        f.readline().strip(),
    ]


def get_size(shape):
    size = 0
    for line in shape:
        size += line.count('#')
    return size


shapes, tree = parse_input('input/day12.txt')

ok_count = 0

for t in tree:
    total_space_needed = 0

    for shape_idx in range(len(shapes)):
        total_space_needed += get_size(shapes[shape_idx]) * t[2][shape_idx]

    if total_space_needed > t[0] * t[1]:
        print('too large')
    elif sum(t[2]) * 9 <= t[0] * t[1]:
        print('ok', t[0], t[1])
        ok_count += 1

    else:
        print('hmmm')


print(ok_count)
