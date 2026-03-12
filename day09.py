def load_points(filename):
    points = []
    with open(filename) as f:
        for line in f:
            x, y = line.split(',')
            x = int(x)
            y = int(y)
            points.append((x, y))
    return points


def points_to_edges(points):
    edges = []

    for idx in range(1, len(points)):
        start = points[idx - 1]
        end = points[idx]

        edges.append((start, end))

    edges.append((points[-1], points[0]))

    return edges


def get_outside_squares(edges):
    outside = set()
    border = set()
    for edge in edges:
        match get_direction(edge):
            case 'n':
                x = edge[0][0]
                for y in range(edge[1][1], edge[0][1] + 1):
                    border.add((x, y))
                    outside.discard((x, y))
                    if (x - 1, y) not in border:
                        outside.add((x - 1, y))
            case 's':
                x = edge[0][0]
                for y in range(edge[0][1], edge[1][1] + 1):
                    border.add((x, y))
                    outside.discard((x, y))
                    if (x + 1, y) not in border:
                        outside.add((x + 1, y))
            case 'e':
                y = edge[0][1]
                for x in range(edge[0][0], edge[1][0] + 1):
                    border.add((x, y))
                    outside.discard((x, y))
                    if (x, y - 1) not in border:
                        outside.add((x, y - 1))
            case 'w':
                y = edge[0][1]
                for x in range(edge[1][0], edge[0][0] + 1):
                    border.add((x, y))
                    outside.discard((x, y))
                    if (x, y + 1) not in border:
                        outside.add((x, y + 1))

    return outside


def get_direction(edge):
    if edge[0][0] == edge[1][0]:
        if edge[0][1] < edge[1][1]:
            return 's'
        else:
            return 'n'
    else:
        if edge[0][0] < edge[1][0]:
            return 'e'
        else:
            return 'w'


def get_largest_square(points):
    max_square_size = calculate_size(points[0], points[1])
    outside = get_outside_squares(points_to_edges(points))

    for p1_idx in range(len(points)):
        print(p1_idx)
        for p2_idx in range(p1_idx + 1, len(points)):
            p1 = points[p1_idx]
            p2 = points[p2_idx]

            if calculate_size(p1, p2) > max_square_size and is_valid_square(p1, p2, outside):
                max_square_size = calculate_size(p1, p2)

    return max_square_size


def calculate_size(p1, p2):
    width = abs(p1[0] - p2[0]) + 1
    height = abs(p1[1] - p2[1]) + 1
    return width * height


def is_valid_square(p1, p2, outside):
    top = min(p1[1], p2[1])
    bottom = max(p1[1], p2[1])
    left = min(p1[0], p2[0])
    right = max(p1[0], p2[0])

    for p in outside:
        if left <= p[0] <= right and top <= p[1] <= bottom:
            return False

    return True



points = load_points('input/day09.txt')
edges = points_to_edges(points)

print(get_largest_square(points))
