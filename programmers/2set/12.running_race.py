def solution(players, callings):

    # 인덱스 찾기 쉽도록 player 별로 index 딕셔너리에 추가
    players_index_dict = { value: index for index, value in enumerate(players) }

    for called_player in callings:

        current_index = players_index_dict[called_player]
        previous_index = current_index - 1

        previous_player = players[previous_index]

        players[previous_index], players[current_index] = players[current_index], players[previous_index]
        players_index_dict[previous_player], players_index_dict[called_player] = current_index, previous_index
        # players_index_dict[previous_player] = current_index
        # players_index_dict[current_index] = previous_index

        # 인덱스 값만 구해서 깔끔하게 처리할 수 있었을 듯
        # now_player_index = players_index_dict[called_player]
        # before_player = players[now_player_index-1]

        # players[players_index_dict[called_player]-1], players[now_player_index] = players[now_player_index], players[players_index_dict[called_player]-1]
        # players_index_dict[before_player], players_index_dict[called_player] = now_player_index, now_player_index -1
    print(players)  

    return players
a = solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])