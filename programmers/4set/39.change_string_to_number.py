def solution(s):

    # 숫자 사전
    number_dict = { 'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }

    # 숫자 사전 순회하면서 있는지 확인해서 replace
    for i in number_dict:
        if i in s:
            s = s.replace(i, str(number_dict[i]))

    return int(s)
    # print(s)

a = solution("one4seveneight")
print(a)