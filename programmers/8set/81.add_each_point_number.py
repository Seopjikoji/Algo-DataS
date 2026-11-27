def solution(n):

    # 정답
    answer = 0 

    # 순회하면서 각 자릿 수 더하기
    for i in str(n):
        answer += int(i)

    return answer

a = solution(123)
print(a)