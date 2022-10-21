from day_03a import solution as solution_day3


def read_input(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        entries = [entry.strip().split() for entry in lines]
        commands = map(lambda e: (str(e[0]), int(e[1])), entries)

    return commands


input = read_input('input_day_03_part1.txt')

# result = solution_part1(input)

# print(f"result part 1: {result}")

# part 2
result_2 = solution_day3(input)

print(f"result part 2: {result_2}")
