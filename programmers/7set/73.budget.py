# from itertools import combinations

def solution(d, budget):

    # 부서 전체 수
    # part_num = len(d)

    # # 시간 초과
    # # 지원 가능 부서 수
    # # supportable_part_num = 0

    # for i in range(part_num, 0, -1):
    #     for a in combinations(d, i):
    #         if budget >= sum(a):
    #             return i
    # return 0
    
    # 오름차순으로 정렬, 최대한 많은 부서를 포함하기 위해서는 예산이 적은 부서부터 예산 배청이 필요
    d.sort()

    # while 문

    # 예산
    sum_budget = 0
    
    # # 배열 index
    # index = 0

    # while sum_budget < budget:
    #     # print(sum_budget)
    #     sum_budget += d[index]
    #     if sum_budget <= budget:
    #         index += 1
    #     if index + 1 > part_num:
    #         break

    # return index

    # for 문

    # 부서 수 count
    part_count = 0

    for i in d:
        print(i)
        sum_budget += i
        if budget >= sum_budget:
            part_count += 1
        else:
            break

    return part_count

a = solution([1, 3, 2, 5, 4], 10)
print(a)