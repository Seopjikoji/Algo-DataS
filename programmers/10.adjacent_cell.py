def solution(board, h, w):
    answer = 0
    
    cell_count = len(board)
    target_color = board[h][w]

    same_count = 0

    dh = [-1, 1, 0, 0]
    dw = [0, 0, -1, 1]
    
    for i in range(0, 4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        # print(h_check, w_check)
        if 0 <= h_check < cell_count and 0 <= w_check < cell_count:
            if board[h_check][w_check] == target_color:
                same_count += 1

    answer = same_count
    return answer

a = solution(
    [["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]],
    0,
    1
    )

print(a)