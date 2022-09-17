def solution(measurements):
    if len(measurements) <= 3:
        return sum(measurements)
    i = 1
    j = 3
    prev_window_sum = sum(measurements[0:3])

    increments = 0

    while i <= len(measurements) - 3:
        window_sum = prev_window_sum - measurements[i-1] + measurements[j]
        if window_sum > prev_window_sum:
            increments += 1
        i += 1
        j += 1
        prev_window_sum = window_sum

    return increments
