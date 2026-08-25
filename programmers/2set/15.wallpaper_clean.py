def solution(wallpaper):

    # 바탕화면 규격(세로, 가로)
    h, w = len(wallpaper), len(wallpaper[0])

    # 파일 인덱스 배열(세로, 가로 각각)
    h_index =[]
    w_index =[]

    # 순회하면서 파일 인덱스 구하기 
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j] == '#':
                h_index.append(i)
                w_index.append(j)

    # print(h_index)
    # print(w_index)
    lux, luy, rdx, rdy = min(h_index), min(w_index), max(h_index) + 1, max(w_index) + 1

    return [lux, luy, rdx, rdy]

a = solution(["..", "#."])

print(a)