def solution(array, commands):

    # 정답 배열
    answer = []

    # 순회
    for i in commands:
        num_list = array[i[0]-1:i[1]]

        # 오름차순 정렬
        num_list.sort()
        # k번째 수
        answer.append(num_list[i[2]-1])

    return answer


a = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(a)