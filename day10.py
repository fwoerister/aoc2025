import re
from heapq import heappush, heappop

from z3 import *


class Machine:
    def __init__(self, indicators=None, buttons=None, joltages=None):
        self.indicators_goal = indicators if indicators else []
        self.indicators_state = ['.'] * len(self.indicators_goal)
        self.buttons = buttons if buttons else []
        self.joltages_goal = joltages if joltages else []
        self.joltages_state = [0] * len(self.joltages_goal)


def read_machines(path):
    with open(path) as f:
        return [parse_machine(line) for line in f]


def parse_machine(line):
    indicators = []
    buttons = []
    joltages = []

    indicators_regex = r'\[([.#]+)\]'
    buttons_regex = r'(\([0-9]+(?:,[0-9]+)*\))'
    joltages_regex = r'\{(.+)\}'

    result = re.findall(indicators_regex, line)
    indicators.extend(list(result[0]))

    result = re.findall(buttons_regex, line)

    for button in result:
        parsed_button = [int(val) for val in button[1:-1].split(',')]
        buttons.append(parsed_button)

    result = re.findall(joltages_regex, line)
    joltages.extend([int(joltage) for joltage in result[0].split(',')])

    return Machine(indicators, buttons, joltages)


def find_min_button_presses_to_reach_indicator_goal(machine):
    # (button_count, buttons, current, goal)

    buttons = machine.buttons
    visited = set()

    states = []
    heappush(states, (0, "".join(machine.indicators_state), "".join(machine.indicators_goal)))

    while states:
        current = heappop(states)

        if current[1] == current[2]:
            return current[0]

        for button in buttons:
            next_state = press_button(list(current[1]), button)
            if next_state not in visited:
                heappush(states, (current[0] + 1, next_state, current[2]))
            visited.add(next_state)
    return -1


def find_min_button_presses_to_reach_joltages_goal(machine):
    variables = [Int(f'p{idx}') for idx in range(len(machine.buttons))]

    opt = Optimize()

    for idx in range(len(machine.joltages_goal)):
        connected_buttons = []

        for button_idx in range(len(machine.buttons)):
            if idx in machine.buttons[button_idx]:
                connected_buttons.append(variables[button_idx])

        opt.add(sum(connected_buttons) == machine.joltages_goal[idx])


    opt.minimize(sum(variables))
    print(opt.check())
    model = opt.model()

    total_presses = 0

    for variable in variables:
        total_presses += model[variable].as_long()

    return total_presses


def is_valid(state, goal):
    for idx in range(len(state)):
        if state[idx] > goal[idx]:
            return False
    return True


def press_joltages_button(state, button):
    for idx in button:
        state[idx] += 1
    return list(state)


def press_button(state, button):
    for idx in button:
        state[idx] = '.' if state[idx] == '#' else '#'
    return "".join(state)


machines = read_machines('input/day10.txt')

total = 0
for m in machines:
    presses = find_min_button_presses_to_reach_joltages_goal(m)
    print(presses)
    total += presses

print(total)
