A, B = map(int, input().split())

num_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result_list = []

while A > 0:
    result_list.append(num_list[A%B])
    A = A//B

print(''.join(reversed(result_list)))

# while B <= A:
#     result_list.append(num_list[A%B])
#     A = A//B
#     if B > A:
#         result_list.append(num_list[A])
    
# print(''.join(reversed(result_list)))