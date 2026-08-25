def solution(name, yearning, photo):

    # 사진 순서대로 점수 결과 값 List
    yearning_score_by_photo = []

    # 그리워하는 사람별 스코어 Dictionary 생성
    yearning_score_by_persion = { value: yearning[index] for index, value in enumerate(name)}
    print(yearning_score_by_persion)

    # 순회하면서, 사진별로 인물이 그리워하는 사람 목록 내에 있는지 체크하고, 존재하는 인물들에 대한 점수를 더해준다.
    for ind_photo in photo:
        yearning_score = 0
        for person in ind_photo:
            if person in yearning_score_by_persion:
                yearning_score += yearning_score_by_persion[person]
        yearning_score_by_photo.append(yearning_score)

    return yearning_score_by_photo            
        
a = solution(
    ["kali", "mari", "don"],
    [11, 1, 55],
    [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
    )

print(a)