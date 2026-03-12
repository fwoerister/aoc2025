import operator
import re
from functools import reduce


def parse_exercises(path):
    operands = []
    operators = []
    with open(path) as f:
        line = f.readline()

        while line:
            splitted_line = re.split(" +", line.strip())
            if splitted_line[0].isdigit():
                splitted_line = [int(val) for val in splitted_line]
                operands.append(splitted_line)
            else:
                operators = splitted_line

            line = f.readline()
    return operands, operators


def parse_exercises_part_2(path):
    exercises = []

    with open(path) as f:
        lines = [l.strip() for l in f.readlines()]

        for op in re.split(r" +", lines[-1].strip()):
            exercises.append([op, []])

        operands = []
        current_exercise = 0
        for col_idx in range(len(lines[0])):
            current_operand = ""
            for row_idx in range(len(lines) - 1):
                current_operand += lines[row_idx][col_idx]
            if current_operand.strip().isdigit():
                operands.append(int(current_operand))
            else:
                exercises[current_exercise][1] = operands
                operands = []
                current_exercise += 1

        exercises[current_exercise][1] = operands
    return exercises


def transform_to_math_exercises(operands, operators):
    exercises = []
    for col_idx in range(len(operands[0])):
        current_exercise = (operators[col_idx], [])
        for row_idx in range(len(operands)):
            current_exercise[1].append(operands[row_idx][col_idx])
        exercises.append(current_exercise)
    return exercises


def solve(exercises):
    print(exercises)
    results = []
    for exercise in exercises:
        match exercise[0]:
            case '+':
                results.append(sum(exercise[1]))
            case '*':
                results.append(reduce(operator.mul, exercise[1], 1))

    print(results)
    return sum(results)


ex = parse_exercises_part_2("input/day06.txt")
print(solve(ex))
