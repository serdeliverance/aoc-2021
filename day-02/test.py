from day_02 import solution

# TODO extract this logic into utils function
with open('input.txt', 'r') as f:
    lines = f.readlines()
    entries = [entry.strip().split() for entry in lines]
    commands = map(lambda e: (str(e[0]), int(e[1])), entries)

result = solution(commands)

print(result)
