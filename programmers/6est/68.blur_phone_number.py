def solution(phone_number):

    # 정답 문자열 초기화
    answer = ''

    # 휴대폰 번호 길이
    len_phone = len(phone_number)

    answer = ('*' * (len_phone - 4)) + phone_number[-4:]

    return answer

a = solution('027778888')
print(a)