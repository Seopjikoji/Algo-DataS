def solution(k, m, score):

    # 내림차순으로 큰 것 부터 정리
    desc_score = sorted(score, reverse=True)

    # 이익 초기화
    # profit = 0

    # 어차피 내림차순으로 배열되었으므로, m-1번 부터 m 씩 인덱스 순회하면서 값 더해주면 됨
    profit = sum(desc_score[m-1::m]) * m
    
    # 점수 순회 돌면서 마지막 인덱스일 때만 체크하면 되는 건가 ?
    # for index, value in enumerate(desc_score):
        
    #     if len(box) % m == 0:
    #         profit += min(box) * m
    #         box = []

    # return profit
    print(profit)

a = solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2, 1, 2])