import sys


def get_invalid_id_sum(start, end):
    sum = 0
    for id_val in range(start, end + 1):
        if is_invalid_id(id_val):
            sum += id_val

    return sum


def is_invalid_id(id_number):
    id_str = str(id_number)

    pattern_len = 1

    while pattern_len <= len(id_str) // 2:
        pattern = id_str[:pattern_len]
        factor = len(id_str) // pattern_len

        if id_str == pattern * factor:
            return True

        pattern_len += 1

    return False


with open(sys.argv[1]) as f:
    line = f.readline()
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in line.split(',')]

    sum = 0

    for r in ranges:
        sum += get_invalid_id_sum(r[0], r[1])

    print(sum)
