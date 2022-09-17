def solution(commands):
    horizontal = 0
    depth = 0
    aim = 0

    for c in commands:
        match c[0]:
            case 'down':
                aim += c[1]
            case 'up':
                aim -= c[1]
            case 'forward':
                horizontal += c[1]
                depth += aim * c[1]

    return horizontal * depth
