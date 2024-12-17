N, M = map(int, input().split())

A_mat = []
B_mat = []

before_result_mat = []
result_mat = []

for i in range(2*N):
    a = list(map(int, input().split()))
    if i <= N-1:
        A_mat.append(a)
    else:
        B_mat.append(a)

for j in range(len(A_mat)):
    for k in range(len(A_mat[j])):
        before_result_mat.append(A_mat[j][k]+B_mat[j][k])
    result_mat.append(before_result_mat)
    before_result_mat=[]


for a in range(len(result_mat)):
    result_str = ' '.join(map(str,result_mat[a]))
    print(result_str)

# numbers = [10, 20, 30]

# s = ''.join(map(str, numbers))
# print(s)
# print(A_mat)
# print(B_mat)
# print(result_mat)

#복습
# N, M = map(int, input().split())

# A_mat_2 = []
# B_mat_2 = []

# b_result_mat = []
# r_result_mat = []

# for i in range(N):
#     A = list(map(int, input().split()))
#     A_mat_2.append(A)

# for j in range(N):
#     B = list(map(int, input().split()))
#     B_mat_2.append(B)

# #더해주면서 출력도 가능하겠네
# for k in range(N):
#     for l in range(M):
#     #     print(A_mat_2[k][l] + B_mat_2[k][l], end=' ')
#     # print()
#         b_result_mat.append(A_mat_2[k][l] + B_mat_2[k][l])
#     r_result_mat.append(b_result_mat)
#     b_result_mat = []

# for m in range(len(r_result_mat)):
#     print(' '.join(map(str,r_result_mat[m])))


