from string import ascii_lowercase

alphabet_list = list(ascii_lowercase)

A = input()

for i in range(len(alphabet_list)):
    print(A.find(alphabet_list[i]), end = ' ')

# 아스키 코드 이용 1

# A = input()
# a = ord('a')

# for i in range(26):
#     print(A.find(chr(a+i)), end = ' ')

# 아스키 코드 이용 2
# A = input()
# check = [-1]*26

# for i in range(len(A)):
#     print(check[ord(A[i])-97])
#     if check[ord(A[i])-97] != -1:
#         continue
#     else:
#         check[ord(A[i])-97] = i

# for i in range(len(check)):
#     print(check[i], end = ' ') 