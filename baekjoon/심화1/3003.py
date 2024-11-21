chess_list = list(map(int, input().split()))

for i in range(6):
    if i < 2:
        print(1-chess_list[i], end=' ')
    elif i < 5:
        print(2-chess_list[i], end=' ')
    else:
        print(8-chess_list[i], end=' ')

            
    