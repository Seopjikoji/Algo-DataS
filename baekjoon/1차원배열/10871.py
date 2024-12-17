# A, B = map(int, input().split())

# N_list = list(map(int,input().split()))

# C = ""

# for i in range(A):
#     if B > N_list[i]:
#         C+=str(N_list[i])+" "

# # i=0
# # while i<A:
# #     if B > N_list[i]:
# #         print(N_list[i],end=" ") 
# #         # C+=str(N_list[i])+" "+"A" 
# #         # print(C)   
# #     i+=1 


# print(C)

#새롭게 알게된 사실
# print(N_list[i],end=" ") 이런식으로 작성하면 기본 옵션인 \n 이 되지 않고 공백만 생김 

#복습
# temp_list = []

# A, B = map(int, input().split())
# N_list = input().split()

# for i in range(len(N_list)):
#     if B > int(N_list[i]):
#         temp_list.append(N_list[i])
    
# print(' '.join(temp_list))