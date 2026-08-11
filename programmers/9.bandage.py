def solution(bandage, health, attacks):

    # 최대 순회 시간 구하기
    max_time = attacks[-1][0]
    # print(max_time)

    # 최대 회복 가능 체력
    max_health = health

    # 최대 최력 회복 횟수
    max_health_recovery_count = bandage[0]

    # 체력 회복 연속 성공 횟수
    health_recovery_continuous_success_count = 0

    # 공격을 했는지 안했는지 로그를 남겨야 하나 ? 비교해야하는 attacks 로그의 인덱스를 기록하는게 나을 듯
    current_attack_index = 0

    # 시간별로 순회하면서 체력, 연속 성공 횟수를 구해야 함
    for time in range(1, max_time + 1):
        if attacks[current_attack_index][0] == time:
            health -= attacks[current_attack_index][1]
            health_recovery_continuous_success_count = 0
            if health <= 0:
                return -1
            current_attack_index += 1
        else:
            health = min(max_health, health + bandage[1])
            health_recovery_continuous_success_count += 1
            if max_health_recovery_count == health_recovery_continuous_success_count:
                health = min(max_health, health + bandage[2])
                health_recovery_continuous_success_count = 0

        # print(time, health, health_recovery_continuous_success_count)

    return health        

        
        


a = solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
print(a)