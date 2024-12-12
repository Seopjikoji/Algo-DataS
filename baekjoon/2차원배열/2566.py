max_num = 0
max_place = []

for i in range(9):
    A = list(map(int, input().split()))
    if max(A) >= max_num:
        max_num = max(A)        
        max_place = [i+1, A.index(max_num)+1]


print(max_num)
print(' '.join(map(str,max_place)))