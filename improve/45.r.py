# 10진법 > 타 진법으로 바꾸는 방법임
def base_converter(num, base):

    # 결과
    result = ''
    # reverse_result = ''

    # num 대상 수, base 진법
    while num:
        result = str(num % base) + result
        # reverse_result += str(num % base)
        num //= base

    return int(result)

def solution(n):

    # 3진법으로 변환
    tenary = str(base_converter(n, 3))
    print(tenary)

    # 뒤집기
    reversed_tenary = ''.join(reversed(tenary))
    print(int(reversed_tenary))
    # 10진법으로 변환(타 진법에서 10진법으로 변환하는거 X)
    # result = base_converter(int(reversed_tenary), 10)
    # return result
    # reversed_tenary2 = ''.join(sorted(tenary, reverse=True))
    # print(reversed_tenary)
    # print(reversed_tenary2)

# a = base_converter(45, 3)

# print(a)

a = solution(45)