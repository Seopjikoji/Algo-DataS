A = int(input())

score_list = list(map(int,input().split()))
new_total = 0

for i in range(A):

    new_total = new_total + score_list[i]

print(new_total/max(score_list)*100/A)