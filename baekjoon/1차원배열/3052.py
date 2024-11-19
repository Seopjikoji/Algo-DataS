divided_list = []

for i in range(10):
    A = int(input())
    divided_list.append(A%42)

removed_dupl_list = set(divided_list)

print(len(removed_dupl_list))

# print(len(set(divided_list)))

