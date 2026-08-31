# 약수 개수 세는 함수
def cal_divisor_count(n):
    divisor_list = []
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            divisor_list.append(i)
            if i != n // i:
                divisor_list.append(n // i)
    return len(divisor_list)

def solution(number, limit, power):

    # 기사단원별 약수 개수 list
    knight_divisor_list = []

    # 순회하면서, 기사단원별 약수 리스트 생성
    for i in range(1, number+1):
        knight_divisor_list.append(cal_divisor_count(i))

    # 기사단원별 공격력 리스트 생성(제한 공격력 반영한 보정 공격력 리스트)
    knight_attack_power_list = []

    # 위랑 통합할 수도 있기는 한데 분리해서 생각해보자 우선    
    for i in knight_divisor_list:
        if limit < i:
            knight_attack_power_list.append(power)
        else:
            knight_attack_power_list.append(i)

    return sum(knight_attack_power_list)


a = solution(5, 3, 2)
print(a)