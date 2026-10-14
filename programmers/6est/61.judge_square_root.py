def solution(n):

    # n 이 어떤 양의 정수 x 의 제곱인지 판단
    print(int(n**(1/2)))
    square_root = int(n**(1/2))

    if square_root**2 == n:
        return (square_root+1)**2
    else:
        return -1


a = solution(3)
print(a)