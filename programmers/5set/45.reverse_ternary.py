def solution(n):

    # 3진법 만들 때 필요한 수
    ternary_list = []

    # while문 반복하면서 3진법 수 담기
    while n >= 3:
        ternary_list.append(n % 3)
        n //= 3
        if n < 3:
            ternary_list.append(n)

    # 0 아닌 것만 골라내기 > 이게 잘못됨
    # ternary_list = [ i for i in ternary_list if i != 0 ]
    tenary_str = ''.join(map(str, ternary_list))

    # 십진법 변환 decimal
    decimal = 0 if ternary_list else n
    index_start = len(tenary_str)-1

    # 순회하면서 10진수로 전환
    for i in tenary_str:
        decimal += int(i) * (3**(index_start))
        index_start -= 1

    return decimal


a = solution(125)
print(a)