def solution(n):

    # n을 1부터 n-1 까지 나눔, 시간 복잡도 n, n 범위: 3 <= n <= 1,000,000
    for i in range(1, n):
        if n % i == 1:
            return i

a = solution(12)
print(a)