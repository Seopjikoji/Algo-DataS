def solution(absolutes, sign):

    # 결과값
    sum = 0

    # 절대값들(absolutes) 순회하면서, 각각의 sign(부호) 판단, 양수이면 더하고, 음수면 -1 곱해서 더하기
    for index, value in enumerate(absolutes):
        if sign[index]:
            sum += value
        else:
            sum += value * -1

    return sum

