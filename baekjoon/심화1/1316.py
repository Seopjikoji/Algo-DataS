A = int(input())

temp_list = []
count = 0


for i in range(A):
    B = input()
    C = list(set(B))
    
    is_group_word = True

    for j in C:
        temp_list = []
        for k in range(len(B)):
            if j == B[k]:
                temp_list.append(k)

   # temp_list의 길이가 2 이상일 때, 인덱스 차이를 확인
        if len(temp_list) >= 2:
            temp_list.reverse()
            for t in range(0, len(temp_list)-1):
                if temp_list[t] - temp_list[t+1] > 1:
                    is_group_word = False  # 그룹 단어가 아니면 False로 설정
                    break  # 더 이상 확인할 필요 없이 종료
            if not is_group_word:
                break  # 그룹 단어가 아니면 더 이상 다른 문자를 확인할 필요 없음

    if is_group_word:
        count +=1

print(count)                    
        # print(B[j])
        # print(B.index(B[j],j+1,len(B)))
        # print(B.index(B[j]))
        # if B.index(B[j],j+1) - B.index(B[j]) >=2:
        #     print('그룹단어 아님')

# B = 'abca'

# print(B.index(B[0],0,len(B)))
# 그룹단어인지 아닌지 체크해서 아니면 뺴는 방식으로

# for i in range(A):
#     word = input()
#     for j in range(len(word)-1):
#         if word[j] == word[j+1]:
#             pass
#         elif word[j] in word[j+1:]:
#             A-=1
#             break

# print(A)