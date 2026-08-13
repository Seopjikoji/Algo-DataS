def solution(data, ext, val_ext, sort_by):

    #기준 정보 담긴 딕셔너리 생성
    standard_data = { 'code': 0, 'date': 1, 'maximum': 2, 'remain': 3 }

    #분류 및 정렬 인덱스 추출
    sort_index = standard_data[ext]
    arrange_index = standard_data[sort_by]

    # 분류된 결과 추출
    sort_result = []

    for index in range(len(data)):
        if data[index][sort_index] < val_ext:
            sort_result.append(data[index])

    #분류된 결과 정렬
    arrange_result = sorted(sort_result, key=lambda x: x[arrange_index])

    return arrange_result

a = solution(
    [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]],
    "date",
    20300501,
    "remain",
)

print(a)