def solution(n, m, section):

    # 최대 간격 설정
    # 순회 시작 지점
    start = section[0]

    # 순회 변동 지점(변동 가능, 초기 지점 초기화)
    next = start

    # 덧칠 횟수
    repaint_count = 0

    # 다시 칠해야 하는 구역 순회
    for i in section:
        print(i, next, n)
        if next > n:
            break
        
        if i == next:
            next += m
            repaint_count += 1
        elif i > next:
            next = i

    return repaint_count


a = solution(8, 4, [2, 3, 6])
print(a,'s')

# def solution(n, m, section):

#     # 최대 간격 설정
#     # 순회 시작 지점
#     start = section[0]

#     # 순회 변동 지점(변동 가능, 초기 지점 초기화)
#     next = start

#     # 덧칠 횟수
#     repaint_count = 0

#     # 다시 칠해야 하는 구역 순회
#     for i in section:
#         if next == start:
#             next = i + m - 1
#             repaint_count += 1
#         elif i > next:
#             repaint_count += 1
#             next = i + m - 1
            
        

#     return repaint_count


# a = solution(8, 4, [2, 3, 6])
# print(a,'s')


def solution(n, m, section):
    # 첫 시작
    start = section[0]

    # 덧칠 횟수
    repaint_count = 0

    # 롤러 위치
    r_location = start

    # 순회
    for s in section:
        if r_location == start:
            repaint_count += 1
            r_location = s + m - 1

        if r_location < s:
            repaint_count += 1
            r_location = s + m - 1

    return repaint_count