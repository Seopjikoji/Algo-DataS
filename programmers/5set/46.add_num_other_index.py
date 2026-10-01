from itertools import combinations

def solution(numbers):

    # 합 리스트
    sum_list = []

    # 두 개씩 조합
    for i in combinations(numbers, 2):
        print(i)
        sum_list.append(sum(i))

    return sorted(set(sum_list))
    # print(set(sum_list))

# 다른 아이디어
# def solution(numbers):
    
#     # 합 리스트
#     sum_list = []

#     for i, v in enumerate(numbers):
#         for j in range(i+1, len(numbers)):
#             sum_list.append(v + numbers[j])

#     return sorted(set(sum_list))


a = solution([2, 1, 3, 4, 1])