A, B = map(int, input().split())

basket_list=[]
#원하는 길이의 리스트 만들기
for i in range(A):
    basket_list.append(0)

for j in range(B):
    A, B, C = map(int, input().split())
    if A == B:
        basket_list[A-1] = C
    else:
        for k in range(A-1, B):
            basket_list[k] = C

# 코드를 더 간결하게 쓸 수 있는지 고민, 검산 과정도 필요
# for j in range(B):
#     A, B, C = map(int, input().split())
#     for k in range(A, B+1):
#         basket_list[k-1] = C

print(" ".join(map(str, basket_list)))

