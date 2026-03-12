def get_neighbours(grid, row, col):
    return "".join([
        get_position(grid, row - 1, col - 1),
        get_position(grid, row - 1, col),
        get_position(grid, row - 1, col + 1),
        get_position(grid, row, col - 1),
        get_position(grid, row, col + 1),
        get_position(grid, row + 1, col - 1),
        get_position(grid, row + 1, col),
        get_position(grid, row + 1, col + 1),
    ])


def get_position(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    return ""


def remove_rolls(grid):
    count = 0
    removed_rolls = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            neighbours = get_neighbours(grid, row, col)
            if grid[row][col] == '@' and neighbours.count('@') < 4:
                removed_rolls.append((row, col))
                count += 1

    for roll in removed_rolls:
        grid[roll[0]][roll[1]] = 'x'
    return count


with open('input/day04.txt') as f:
    grid = f.readlines()

    grid = [list(row) for row in grid]

    total = 0

    count = remove_rolls(grid)
    total += count

    while count > 0:
        count = remove_rolls(grid)
        total += count

    print(total)
