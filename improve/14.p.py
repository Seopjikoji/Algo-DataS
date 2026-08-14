def find_start_index(park, h, w):
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                return i, j
            
def solution(park, routes):
    h, w = len(park), len(park[0])

    direction_index_dict = { 'E': 0, 'W': 1, 'S': 2, 'N': 3 }

    y = 0
    x = 0

    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]

    y, x = find_start_index(park, h, w)

    print(y, x, '시작 위치')
    for route in routes:
        direction, delta = route.split()
        delta = int(delta)
        direction_index = direction_index_dict[direction]
        print(direction_index, 'index', direction, 'direction')
        
        ny, nx = y, x

        is_pass = True

        for _ in range(delta):
            print('delta', delta)
            # 시작점에서 수행
            ny = ny + dy[direction_index]
            nx = nx + dx[direction_index]
            print(ny, nx, '현재 위치')
            # 조건 안맞으면 해당 delta 값 순차 진행하다가 이탈하면 됨
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                is_pass = False
                break

            # X 인지 체크      
            if park[ny][nx] == 'X':
                is_pass = False
                break

        if is_pass:    
            y = ny
            x = nx
        print(y, x, '패스 여부에 따른 delta 이동 후 위치')
    return [y, x]        

    # print(ny, nx)

a = solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"]	)
print(a)