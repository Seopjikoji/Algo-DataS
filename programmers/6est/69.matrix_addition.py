def solution(arr1, arr2):

    # 정답 배열
    answer_arr = []

    # 행렬 길이
    row = len(arr1)
    col = len(arr1[0])

    # # 행렬 순회하면서 각 값 더하기
    for i1 in range(row):
        arr = []
        for i2 in range(col):
            arr.append(arr1[i1][i2] + arr2[i1][i2])

        # 결과 더하기
        answer_arr.append(arr)
        
    return answer_arr
    

    # # 행렬 순회하면서 각 값 더하기
    # for i1, v1 in enumerate(arr1):
    #     arr = []
    #     for i2, v2 in enumerate(arr2):
    #         arr.append(arr1[i1][i2] + arr2[i1][i2])

    #     # 결과 더하기
    #     answer_arr.append(arr)


a = solution([[1], [2]], [[3], [4]])
print(a)