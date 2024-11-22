A = int(input())

A_list = []

for i in range(2*A-1):
    if 2*A-1 >= 2*i+1:
        A_list.append(2*i+1)
        
temp_list = A_list[0:A-1]
temp_list.reverse()

A_list[len(A_list):2*A-1] = temp_list

for j in range(len(A_list)):
    print(" "*(((2*A-1-A_list[j]))//2)+"*"*A_list[j])

#다른 아이디어(더 좋아보임, 증가하는 부분과 감소하는 부분을 나눔, 튜플도 다시 인지함)

# B = int(input())

# for i in range(1,B+1):
#     print(" "*(B-i)+"*"*(2*i-1))
# for j in range(B-1,0,-1):
#     print(" "*(B-j)+"*"*(2*j-1))