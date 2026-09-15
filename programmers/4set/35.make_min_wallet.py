def solution(sizes):

    # 명함의 가로, 세로 길이를 하나씩 순회할 때마다, 그때 그때 판단해서 변수로 기록
    w = 0
    h = 0

    # 모든 명함의 가로, 세로 길이가 담긴 2차원 배열 순회
    for s in sizes:
        # 오름차순, sort() 함수는 list 에만 사용할 수 있음
        s.sort()

        # 오름차순 후 순회하면서 가장 큰 것으로 갱신, 모든 명함을 다 포함해야 하니까
        w = max(s[0], w)
        h = max(s[1], h)

    # 이게 더 깔끔한 듯, sort 안해도 되니깐
    # max_w = 0
    # max_h = 0

    # for s in sizes:
    #     max_w = max(min(s), max_w)
    #     max_h = max(max(s), max_h)

    return w * h

a = solution([[60, 50], [30, 70], [60, 30], [80, 40]])