def solution(price, money, count):

    # 부족한 금액 변수 설정
    short_money = 0

    # 사용한 금액 계산
    use_money = price * sum(i for i in range(1, count+1))

    # 처음 가지고 있던 금액과 놀이기구 count 만큼 타는데 필요한 금액 비교 후 놀이기구 타는데 필요한 금액이 더 크면 차감, 아니면 0 반환
    if money < use_money:
        short_money = use_money - money

    return short_money

a = solution(3, 20, 4)

print(a)