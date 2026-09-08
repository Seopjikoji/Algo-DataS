from itertools import combinations

def solution(number):

    # 조합 내장함수로
    count = 0

    for i, j, k in combinations(number, 3):
        if i + j + k == 0:
            count += 1

    return count

    # # 3개의 서로 다른 수 뽑는 것, 이번 기회에 순열, 중복 함수 기억하자
    # # number 길이 기준으로 인덱스 저장, 어차피 3개만 고르면 되니까, for 문 13 * 13 * 13 이라 시간 복잡도는 크게 상관 없을 듯
    # number_len = len(number)
    # count = 0
    # cases = []

    # for i in range(number_len):
    #     for j in range(number_len):
    #         for k in range(number_len):
    #             if i != j and j != k and i != k:
    #                 # 인덱스 오름차순으로 배열 후 통합
    #                 t = (i, j, k)
    #                 sort = tuple(sorted(t))
    #                 cases.append(sort)
    #                 # if number[i] + number[j] + number[k] == 0:
    #                 #     count += 1
    # # return count // 6
    # # 경우의 수 중복 제거
    # cases = list(set(cases))

    # # 순회하면서 더해서 0 이면 count 증가
    # for case in cases:
    #     if number[case[0]] + number[case[1]] + number[case[2]] == 0:
    #         count += 1

    # return count
    
a = solution([-2, 3, 0, 2, -5])
print(a)