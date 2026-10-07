def solution(board, moves):

    # 터진 인형 개수 count
    count = 0

    # 인형 담을 리스트
    basket = []

    # 순회 시 필요한 범위
    machine_length = len(board)

    # 기계 작동 위치 순회하면서 값들 0 아닌 것까지 이동
    for m in moves:
        print(basket)
        for i in range(machine_length):
            print(i, m-1)
            if board[i][m-1] != 0:
                print(board[i][m-1], '0 아님')
                # print(basket[-1])
                
                if len(basket) != 0 and basket[-1] == board[i][m-1]:
                    count += 2
                    basket.pop()
                    
                else:
                    basket.append(board[i][m-1])
                    
                board[i][m-1] = 0
                break

    return count

a = solution(
    [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
    [1,5,3,5,1,2,1,4]
)

print(a)