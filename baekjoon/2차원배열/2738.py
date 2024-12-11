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