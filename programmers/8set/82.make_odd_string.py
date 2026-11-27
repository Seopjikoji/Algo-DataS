def solution(s):

    # 문자열 쪼개기
    s_list = s.split(' ')

    # 최종 반환된 단어 리스트
    result = []

    # 쪼개진 문자열, 즉, 단어별로 순회하면서 짝수는 대문자로, 홀수는 소문자로 바꾸고 result 에 더함
    for word in s_list:
        changed_word = ''
        for index, c in enumerate(word):
            if index % 2 == 0:
                changed_word += c.upper()
            else:
                changed_word += c.lower()
        result.append(changed_word)

    # 다 끝난 후 list 공백 기준으로 합치기
    return ' '.join(result)
            
            

a = solution("try hello world")
print(a)