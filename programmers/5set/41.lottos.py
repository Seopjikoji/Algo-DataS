def solution(lottos, win_nums):

    # 순위 표 dict
    chart = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 }

    # 있는 개수, 지워진 개수 count
    win_count = 0
    erase_count = 0

    # lottos 번호 순회하면서, 0 아니면서 당첨 숫자에 있는지 확인
    for i in lottos:
        if i != 0:
            if i in win_nums:
                win_count += 1
        else:
            erase_count += 1

    return [chart[win_count+erase_count], chart[win_count]]


a = solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
print(a)