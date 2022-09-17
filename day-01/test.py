from day_01 import solution

with open('input-2.txt', 'r') as f:
    lines = f.readlines()
    measurements = [int(entry.strip()) for entry in lines]

result = solution(measurements)

print(result)
