def solution(n, m, section):

    # 전체 구역 및 구역별 덧칠해야할 부분 표시한 배열, 0은 덧칠 안해도 됨, 1은 덧칠 해야함
    scope = [0] * n

    for i in section:
        scope[i-1] = 1

    # 지울 수 있는 최대 개수
    max_interval = m

    # 덧칠 횟수
    repaint_count = 0
    print(scope, '원본', m, n)
    # while not all(x == 0 for x in scope):
    while not all(x == 0 for x in scope):
        for i in range(0, n - max_interval + 1):
            part = scope[i : i + max_interval]
            print(part, part.count(1), m)
            if part.count(1) == m:
                repaint_count += 1
                for j in range(i, i + max_interval):
                    print('오나?', j)
                    if scope[j] == 1:
                        scope[j] = 0
                        print(m, 'TEST')
                    
            
        m -= 1
    return repaint_count
    print(repaint_count)
    # print(scope, '원본')
    # for i in range(0, n - m + 1):
    #     part = scope[i : i + max_interval]
    #     print(part, part.count(1), m)
    #     if part.count(1) == m:
    #         for j in range(i, i + max_interval):
    #             if scope[j] == 1:
    #                 scope[j] = 0
    #                 m -= 1
    #                 repaint_count += 1
                        


a = solution(8, 4, [2, 3, 6])        