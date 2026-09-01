def solution(k, m, score):

    # 내림차순으로 큰 것 부터 정리
    desc_score = sorted(score, reverse=True)

    # 과일 박스
    box = []

    # 이익 초기화
    profit = 0

    # 점수 순회 돌면서 마지막 인덱스일 때만 체크하면 되는 건가 ?
    for index, value in enumerate(desc_score):
        
        # 과일 담기부터 하는게 나을 듯
        box.append(value)

        # 없어도 되기는 하네.. 왜 ? 어차피 순차적으로 돌다가 m 이랑 개수 다르면 그냥 box 남은 채로 끝남
        # 마지막 인덱스인데, box 안에 과일이 부족할 경우 0 더함
        # if index == len(score) - 1 and len(box) != m:
        #     profit += 0

        # 과일 이익 계산, 계산 후 초기화
        if len(box) % m == 0:
            profit += min(box) * m
            box = []

    return profit
    # print(profit)

a = solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2, 1, 2])