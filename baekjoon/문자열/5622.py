alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

A = input()
time = 0

for i in alpabet_list:
    for j in range(len(A)):
        if A[j] in i:
            time = time + alpabet_list.index(i)+3

print(time)

