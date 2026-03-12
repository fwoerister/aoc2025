def parse_splitters(filename):
    with open(filename) as f:
        lines = f.readlines()

    splitters = []

    for row_idx in range(len(lines)):
        current_level = []
        for col_idx in range(len(lines[row_idx])):
            if lines[row_idx][col_idx] == "^":
                current_level.append(col_idx)

        if current_level:
            splitters.append(current_level)

    return splitters


def count_beams(splitter_levels):
    splitting_count = 0
    open_beams = set(splitter_levels[0])
    for level in splitter_levels:
        for splitter in level:
            if splitter in open_beams:
                open_beams.remove(splitter)
                splitting_count += 1
                if splitter - 1 not in open_beams:
                    open_beams.add(splitter - 1)
                if splitter + 1 not in open_beams:
                    open_beams.add(splitter + 1)
    return splitting_count


cache = {}


def count_worlds(splitters, level, beam):
    if (level, beam) in cache:
        return cache[(level, beam)]

    for level_idx in range(level + 1, len(splitters)):
        if beam in splitters[level_idx]:
            left = count_worlds(splitters, level_idx, beam - 1)
            right = count_worlds(splitters, level_idx, beam + 1)

            cache[(level, beam)] = left + right
            return left + right
    return 1


splitter_levels = parse_splitters("input/day07.txt")

print(count_worlds(splitter_levels, -1, splitter_levels[0][0]))
