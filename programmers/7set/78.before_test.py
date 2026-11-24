def solution(answers):

    # 1, 2, 3 번 수포자 패턴
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # count
    a_correct_count = 0
    b_correct_count = 0
    c_correct_count = 0

    # answer 순회하면서 맞는 거 체크
    for index, value in enumerate(answers):
        if value == a[index % 5]:
            a_correct_count += 1
        if value == b[index % 8]:
            b_correct_count += 1
        if value == c[index % 10]:
            c_correct_count += 1

    # 정답
    answer = []

    # 최대 맞춘 개수
    max_correct_count = max(a_correct_count, b_correct_count, c_correct_count)

    # 판단
    if max_correct_count == a_correct_count:
        answer.append(1)

    if max_correct_count == b_correct_count:
        answer.append(2)

    if max_correct_count == c_correct_count:
        answer.append(3)

    return answer


a = solution([1,2,3,4,5])
print(a)