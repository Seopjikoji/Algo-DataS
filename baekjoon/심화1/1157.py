# s = 'Aaaabbbccc'
# b = ''.join(set(s))
# print(b) # cba

# c = s.upper()
# print(c)

A = input().upper()
B = ''.join(set(A))

count_iden_list = []
count_list = []

for i in B:
    count_iden_list.append({ 'name': i, 'value': A.count(i)})
    count_list.append(A.count(i))

C = max(count_list)

if count_list.count(C) == 1:
    for i in range(len(count_iden_list)):
        if count_iden_list[i]['value'] == C:
            print(count_iden_list[i]['name'])
            exit()
else:
    print('?')

#알게된 점
# exit(1)로 함수를 끝내면 런타임 에러 발생, 에러 나서 함수 실행을 중단한 것으로 간주하기 때문
# exit()도 가능, exit(0) 가능

#더 나은 풀이, 나열된 알파벳 순서에 따른 알파벳 각각의 개수 배열도 같이 만들어줬으면, name, value를 쓸 필요가 없었음, 아 이미 그렇게 작성은 되어있는데, 인지를 못했네
for i in B:
    count_list.append(A.count(i))

if count_list.count(max(count_list)) >= 2:
    print('?')
else:
    print(B[count_list.index(max(count_list))])
    