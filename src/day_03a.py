def solution(power_consumption_list):
    gamma_rate_state = {}
    row_len = len(power_consumption_list[0])
    [gamma_rate_state.setdefault(i, (0, 0)) for i in range(row_len)]

    for power_consumption in power_consumption_list:
        for i in range(row_len):
            gamma_rate_state[i] = (gamma_rate_state[i][0] + 1, gamma_rate_state[i][1]) if int(power_consumption[i]) == 0 else (
                gamma_rate_state[i][0], gamma_rate_state[i][1] + 1)

    gamma_str = ""
    epsilon_str = ""

    for key in gamma_rate_state:
        gamma_item = "0" if str(gamma_rate_state[key][0]) > str(
            gamma_rate_state[key][1]) else "1"
        gamma_str += gamma_item
        epsilon_str += "0" if gamma_item == "1" else "1"

    gamma = int(gamma_str, 2)
    epsilon = int(epsilon_str, 2)

    return gamma * epsilon
