def solution(k, score):

    # 명예의 전당 점수 판
    board = []

    # 최하위 점수 모아 놓은 판
    result = []

    # 순회 점수 개수
    score_len = len(score)

    for s in score:
        if len(board) != k:
            board.append(s)
            board.sort(reverse=True)
            result.append(board[len(board)-1])
        else:
            if board[k-1] < s:
                board[k-1] = s
                board.sort(reverse=True)
                result.append(board[k-1])
            else:
                result.append(board[k-1])

    return result

a = solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
print(a)
            