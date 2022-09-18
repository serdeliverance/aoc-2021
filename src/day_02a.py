def solution(commands):
    x = 0
    y = 0

    for c in commands:
        match c[0]:
            case "forward":
                x += c[1]
            case "up":
                updated_pos = y - c[1]
                y = 0 if updated_pos <= 0 else updated_pos
            case "down":
                y += c[1]
            case _:
                raise ValueError("Invalid argument")

    return x * y
