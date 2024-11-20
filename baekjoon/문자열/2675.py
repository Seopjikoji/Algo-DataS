A = int(input())

for i in range(A):
    B, C = input().split()
    for j in range(len(C)):
        print(C[j] * int(B), end = '')
    print()
