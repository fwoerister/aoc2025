def parse_ranges(lines):
    ranges = []

    for line in lines:
        range_str = line.split("-")
        start = int(range_str[0])
        end = int(range_str[1])
        ranges.append((start, end))

    return ranges


def merge_ranges(ranges):
    merged_ranges = []
    ranges.sort()

    current_start = ranges[0][0]
    current_end = ranges[0][1]

    for idx in range(1, len(ranges)):
        current_range = ranges[idx]

        if current_range[0] > current_end:
            merged_ranges.append([current_start, current_end])
            current_start = current_range[0]
            current_end = current_range[1]
        elif current_range[0] <= current_end < current_range[1]:
            current_end = current_range[1]

    merged_ranges.append([current_start, current_end])

    return merged_ranges


def get_range(val, ranges):
    for range in ranges:
        if range[0] <= val <= range[1]:
            return range
    return None


def remove_middle_ranges(start, end, ranges):
    new_ranges = []
    for range in ranges:
        if not (start <= range[0] <= end and start <= range[1] <= end):
            new_ranges.append(range)

    return new_ranges


def parse_ingredients(lines):
    return [int(line) for line in lines]


def is_in_range(val, ranges):
    for range in ranges:
        if range[0] <= val <= range[1]:
            return True

    return False


def is_overlapping(start, end, ranges):
    for range in ranges:
        if start <= range[0] <= end:
            return True
        if start <= range[1] <= end:
            return True
    return False


def part1():
    with open("input/day05.txt") as f:
        lines = f.readlines()
        split_idx = lines.index("\n")
        ranges = parse_ranges(lines[:split_idx])
        ingredients = parse_ingredients(lines[split_idx + 1:])
        count = 0

        for ingredient in ingredients:
            if is_in_range(ingredient, ranges):
                count += 1

        print(count)


def part2():
    with open("input/day05.txt") as f:
        lines = f.readlines()
        split_idx = lines.index("\n")
        ranges = parse_ranges(lines[:split_idx])
        ranges = merge_ranges(ranges)

        total = 0

        for range in ranges:
            total += range[1] - range[0] + 1

        print(total)


if __name__ == "__main__":
    part2()
