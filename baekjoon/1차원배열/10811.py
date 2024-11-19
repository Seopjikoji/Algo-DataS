A, B = map(int, input().split())

basket_num_list = [i for i in range(1, A+1)]

for i in range(B):
    C, D = map(int, input().split())
    temp = basket_num_list[C-1:D]
    temp.reverse()
    basket_num_list[C-1:D] = temp

for j in range(A):
    print(basket_num_list[j], end=" ")

