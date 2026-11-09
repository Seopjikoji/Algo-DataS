from itertools import combinations

def solution(nums):

    # 소수 개수 변수 초기화
    prime_count = 0

    # 개수 조합 착지
    for a, b, c in combinations(nums, 3):
        # 숫자 합 구하기
        sum = a + b + c
        
        # 약수 배열 초기화
        divisor = []

        for i in range(1, int(sum ** 1/2)+1):
            if sum % i == 0:
                divisor.append(i)
                if i != (sum // i):
                    divisor.append(sum // i)

        if len(divisor) == 2:
            prime_count += 1

    return prime_count

a = solution([1, 2, 3, 4])
print(a)