def cal_ind_gift_index(index, gift_count_list):
    give_count = 0
    get_count = 0
    
    for i, value in enumerate(gift_count_list):
        if index == i:
            give_count = sum(value)
        get_count += value[index]

    # print('GIVE', give_count)
    # print('GET', get_count)    

    return give_count - get_count
    
def solution(friends, gifts):
    answer = 0

    # 친구별로 주고 받은 선물 개수를 저장할 2차원 배열 초기화
    give_and_receive_list = [[0] * len(friends) for _ in range(len(friends))]
    get_gift_count_list = []

    # 친구별로 주고 받은 선물 개수를 2차원 배열로 정리
    for i, value in enumerate(friends):
        for j in range(len(gifts)):
            # if i == j:
            #     give_and_receive_list[i][i] = '-'
            sender, receiver = gifts[j].split()
            if sender == value:
                give_and_receive_list[i][friends.index(receiver)] += 1

    # print(give_and_receive_list)    
    # 개별로 선물 받을 선물 수 세기
    for i , value in enumerate(friends):
        ind_count = 0
        for j in range(len(friends)):
            if i != j:
                # print(i, j, give_and_receive_list[i][j], give_and_receive_list[j][i])
                if give_and_receive_list[i][j] > give_and_receive_list[j][i]:
                    ind_count += 1
                if give_and_receive_list[i][j] == give_and_receive_list[j][i]:
                    # print('HERE', i, j,  cal_ind_gift_index(i, give_and_receive_list), cal_ind_gift_index(j, give_and_receive_list))
                    if cal_ind_gift_index(i, give_and_receive_list) > cal_ind_gift_index(j, give_and_receive_list):
                        ind_count += 1
                    # if cal_ind_get_gift_index(i, give_and_receive_list) == cal_ind_get_gift_index(j, give_and_receive_list):
        get_gift_count_list.append(ind_count)

    print(give_and_receive_list)                 
    print(get_gift_count_list)      
               
    answer = max(get_gift_count_list)
    # print(get_gift_count_list)
    return answer


ta = solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
print(ta)