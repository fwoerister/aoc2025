def read_input(path):
    with open(path) as f:
        network = {}

        for line in f:
            machine, successors = line.split(':')

            network[machine.strip()] = [succesor.strip() for succesor in successors.strip().split(' ')]

        return network


cache = {}


def find_all_paths_to_out(network, start, goal, avoid, visited):
    if (start, goal, avoid) in cache:
        return cache[(start, goal, avoid)]

    if start == "out":
        return 0

    total_paths = 0
    for successor in network[start]:
        if successor == goal:
            return 1
        if successor != avoid and successor not in visited:
            total_paths += find_all_paths_to_out(network, successor, goal, avoid, visited + [successor])

    cache[(start, goal, avoid)] = total_paths
    return total_paths


network = read_input("input/day11.txt")

s_to_d = find_all_paths_to_out(network, "svr", "dac", "fft", [])
print(s_to_d)
s_to_f = find_all_paths_to_out(network, "svr", "fft", "dac", [])
print(s_to_f)

d_to_f = find_all_paths_to_out(network, "dac", "fft", None, [])
print(d_to_f)
f_to_d = find_all_paths_to_out(network, "fft", "dac", None, [])
print(f_to_d)

f_to_o = find_all_paths_to_out(network, "fft", "out", "dac", [])
print(f_to_o)
d_to_o = find_all_paths_to_out(network, "dac", "out", "fft", [])
print(d_to_o)

result = s_to_d * d_to_f * f_to_o + s_to_f * f_to_d * d_to_o

print(result)
