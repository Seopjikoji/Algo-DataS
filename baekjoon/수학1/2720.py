A = int(input())

divideArray = [25, 10, 5, 1]
numArray = []
for i in range(A):
    q = int(input())
    numArray.append(q)
    # for j in divideArray:
    #     Q = q // j
    #     D = q % j
    #     q = D
    #     print(Q, end=' ')

for i in range(A):
    q = numArray[i]
    for j in divideArray:
        Q = q // j
        D = q % j
        q = D
        print(Q, end=' ')
    print()  # 각 테스트 케이스마다 줄바꿈

# changes = [25, 10, 5, 1]
# T = int(input())

# for _ in range(T) :
#     C = int(input())
#     res = []

#     for i in changes :
#         res.append(C // i)	# 몫이 개수
#         C = C % i	# 나머지는 다시 C에 저장
        
#     print(*res)

# A, B = map(int, input().split())

# count = 0
# a = A
# while a >= 1:
#     if a == 1:
#         break
#     if a % B == 0:
#         a = a // B
#         count += 1
#     else:
#         a = a - 1
#         count += 1

# print(count)