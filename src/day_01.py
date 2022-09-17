def solution(measurements):
    prev = -1000
    increments = -1
    for m in measurements:
        if m > prev:
            increments += 1
        prev = m
    return increments
