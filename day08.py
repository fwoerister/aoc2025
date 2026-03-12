import math


def parse_junction_boxes(path):
    with open(path) as f:
        return [to_tuple(line) for line in f.readlines()]


def to_tuple(line):
    values = line.split(",")
    return int(values[0]), int(values[1]), int(values[2])


def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


def find_neighbours(junction_boxes):
    neighbours = []

    for box_idx in range(len(junction_boxes)):
        for neighbour in range(box_idx + 1, len(junction_boxes)):
            box = junction_boxes[box_idx]
            neighbour = junction_boxes[neighbour]
            distance = calc_distance(box, neighbour)
            neighbours.append((distance, box, neighbour))

    return neighbours


def merge_circuits(junction_boxes, n):
    neighbours = find_neighbours(junction_boxes)
    circuits = [{box} for box in junction_boxes]

    neighbours.sort(key=lambda pair: pair[0])

    for idx in range(n):
        neighbour = neighbours[idx]

        box_idx = find_box_idx(circuits, neighbour[1])
        neighbour_idx = find_box_idx(circuits, neighbour[2])

        if box_idx != neighbour_idx:
            circuits[box_idx].update(circuits[neighbour_idx])
            circuits.pop(neighbour_idx)

    return circuits


def fully_connect(junction_boxes):
    neighbours = find_neighbours(junction_boxes)
    circuits = [{box} for box in junction_boxes]

    neighbours.sort(key=lambda pair: pair[0])

    for neighbour in neighbours:
        box_idx = find_box_idx(circuits, neighbour[1])
        neighbour_idx = find_box_idx(circuits, neighbour[2])

        if box_idx != neighbour_idx:
            circuits[box_idx].update(circuits[neighbour_idx])
            circuits.pop(neighbour_idx)

        if len(circuits) == 1:
            return neighbour[1][0] * neighbour[2][0]

    return -1


def find_box_idx(circuits, box):
    for idx, circuit in enumerate(circuits):
        if box in circuit:
            return idx
    return -1


jb = parse_junction_boxes("input/day08.txt")

circuits = merge_circuits(jb, 1000)

circuits.sort(key=lambda c: -len(c))
print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))

print(fully_connect(jb))
