def solution(x, n):

    # 정답 담을 배열
    answer = []

    # 순회하면서 등차수열 식 이용
    for i in range(n):
        answer.append(x * (i + 1))

    return answer

a = solution(-4, 2)
print(a)