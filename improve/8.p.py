def solution(friends, gifts):
    n = len(friends)

    # 이름 -> 인덱스
    friend_index = {name: i for i, name in enumerate(friends)}

    # gift_table[i][j] = i가 j에게 준 선물 개수
    gift_table = [[0] * n for _ in range(n)]

    for gift in gifts:
        sender, receiver = gift.split()
        sender_idx = friend_index[sender]
        receiver_idx = friend_index[receiver]
        gift_table[sender_idx][receiver_idx] += 1

    # gift_index[i] = i가 준 선물 수 - i가 받은 선물 수
    gift_index = []

    for i in range(n):
        give_count = sum(gift_table[i])
        receive_count = sum(gift_table[j][i] for j in range(n))
        gift_index.append(give_count - receive_count)

    # next_month[i] = 다음 달에 i가 받을 선물 개수
    next_month = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            i_to_j = gift_table[i][j]
            j_to_i = gift_table[j][i]

            if i_to_j > j_to_i:
                next_month[i] += 1
            elif i_to_j < j_to_i:
                next_month[j] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    next_month[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_month[j] += 1

    return max(next_month)