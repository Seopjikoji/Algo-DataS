def check_obstacle(park, direction, start, delta):
    h = start[0]
    w = start[1]

    if direction == 'E':
        for i in range(w, w + delta + 1):
            if park[h][i] == 'X':
                return False
            
    if direction == 'W':
        for i in range(w, w - delta - 1, -1):
            if park[h][i] == 'X':
                return False

    if direction == 'S':
        for i in range(h, h + delta + 1):
            if park[i][w] == 'X':
                return False

    if direction == 'N':
        for i in range(h, h - delta - 1, -1):
            if park[i][w] == 'X':
                return False

    return True
    
def solution(park, routes):
    # answer = []

    h, w = len(park), len(park[0])
    start_h, start_w = 0, 0
    # direction_index = { 'E': 0, 'W': 1, 'S': 2, 'N': 3 }

    # 시작점 계산하기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                start_h = i
                start_w = j
                break

    # routes 순회하면서 명령 수행하기
    for op in routes:
        direction, delta = op.split()
        delta = int(delta)

        if direction == 'E':
            if start_w + delta >= w or not check_obstacle(park, direction, [start_h, start_w], delta):
                continue
            else: 
                start_w += delta

        if direction == 'W':
            if start_w - delta < 0 or not check_obstacle(park, direction, [start_h, start_w], delta):
                continue
            else: 
                start_w -= delta

        if direction == 'S':
            if start_h + delta >= h or not check_obstacle(park, direction, [start_h, start_w], delta):
                continue
            else: 
                start_h += delta

        if direction == 'N':
            if start_h - delta < 0 or not check_obstacle(park, direction, [start_h, start_w], delta):
                continue
            else: 
                start_h -= delta                
            # print(start_h, start_w)


    return [start_h, start_w]

a = solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]	)
print(a)