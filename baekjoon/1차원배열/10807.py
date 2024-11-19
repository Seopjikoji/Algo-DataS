A = int(input())
B = input()
C = input()

D = B.split()

count = 0
# for i in range(A):
#     if D[i] == C:
#         count+=1

# print(count)

i=0
while i<A:
    if D[i] == C:
        count+=1   
    i+=1 

print(count)

#효율적인 코드
# n = int(input())
# n_list = list(map(int, input().split()))
# v = int(input())

# print(n_list.count(v))


