cache = {}
hits = 0


def get_largest_joltage(bank, length):

    if length == 0:
        return []

    if length == 1:
        return [max(bank)]

    if len(bank) == length:
        return bank

    max_battery = max(bank[:-(length-1)])
    max_pos = bank.index(max_battery)

    return [max_battery] + get_largest_joltage(bank[max_pos + 1:], length - 1)


with open('input/day03.txt') as f:
    banks = f.readlines()
    total = 0
    for bank in banks:
        best_setting = [str(val) for val in get_largest_joltage([int(battery) for battery in bank.strip()], 12)]
        total += int("".join(best_setting))

    print(total)

