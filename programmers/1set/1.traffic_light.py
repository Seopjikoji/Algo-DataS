import math

def solution(signals):

    max_cycle_time = 0
    for G, Y, Z in signals:
        sum_light_time = G + Y + Z
        if max_cycle_time == 0:
            max_cycle_time = sum_light_time
        else:
            max_cycle_time = (max_cycle_time * sum_light_time) // math.gcd(max_cycle_time, sum_light_time)

    # print(max_cycle_time, 'max_cycle_time')

    
    for i in range(max_cycle_time):
        is_yellow = True
        for G, Y, Z in signals:
            sum_light_time = G + Y + Z
            current_time_in_cycle = (i + 1) % sum_light_time

            if G < current_time_in_cycle <= G + Y:
                is_yellow = is_yellow * True
            else:
                is_yellow = is_yellow * False
            # print(is_yellow, 'is_yellow', current_time_in_cycle)
        # print(i, current_time_in_cycle, G, Y, Z, is_yellow)

        if is_yellow:
            return i + 1
    return -1    
    # answer = 0
    # return answer

a = solution([[1, 1, 4], [2, 1, 3], [3, 1, 2], [4, 1, 1]])
print(a, 'answer')