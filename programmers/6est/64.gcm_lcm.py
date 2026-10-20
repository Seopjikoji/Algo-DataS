def solution(n, m):

    # 최솟값 구하기
    limit = min(n, m)

    # 최대공약수, 0 은 안됨
    gcd = 1

    # 최대 공약수 구하기
    for i in range(1, limit + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    # 최소공배수 구하기
    lcm = gcd * (n // gcd) * (m // gcd)

    return [gcd, lcm]

a = solution(4, 4)
print(a)