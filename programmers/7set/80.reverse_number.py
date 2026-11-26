def solution(n):

    answer = []

    # n 문자열로 변화 시킨 후, 뒤부터 읽어서 answer 에 병합
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer

a = solution(12345)
print(a)