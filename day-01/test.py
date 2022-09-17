from day_01 import solution as solution_part1
from day_01_part_2 import solution as solution_part2

with open('input_part1.txt', 'r') as f:
    lines = f.readlines()
    measurements = [int(entry.strip()) for entry in lines]

result_part1 = solution_part1(measurements)

print(f"result part 1: {result_part1}")

with open('input_part2.txt', 'r') as f:
    lines = f.readlines()
    measurements = [int(entry.strip()) for entry in lines]

result_part2 = solution_part2(measurements)

print(f"result part 2: {result_part2}")
