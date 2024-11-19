A, B = map(int, input().split())

basket_num_list = []
for i in range(A):
    basket_num_list.append(i+1)


for j in range(B):
    C, D = map(int, input().split())
    a = basket_num_list[C-1]
    b = basket_num_list[D-1]
    basket_num_list[C-1] = b
    basket_num_list[D-1] = a

for k in range(A):
    print(basket_num_list[k], end=' ')