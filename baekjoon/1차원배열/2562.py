n_list = []
for i in range(9):
    A = int(input())
    n_list.append(A)

# i=0
# while i<9:
#     A = int(input())
#     n_list.append(A)
#     i+=1 

print(max(n_list))
print(n_list.index(max(n_list))+1)

