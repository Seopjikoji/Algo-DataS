A, B = input().split()

C = A[::-1]
D = B[::-1]

if C > D:
    print(C)
else:
    print(D)

#삼항 연산자
# print(C) if C > D else print(D)