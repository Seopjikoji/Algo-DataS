def solution(N, stages):

    # 정답
    answer = []

    # 실패율 담긴 리스트 만들기(단계 별로)
    failure_list = []

    failuser_dict = {}

    # 단계별 순회
    for stage in range(1, N+1):

        # 도달했으나 실패한 유저 수
        fail_user = 0

        # 도달한 유저 수
        arrive_user = 0

        # 유저별 순회
        for user in stages:
            # 해당 stage 도달한 유저 수
            if stage <= user:
                arrive_user += 1
                if stage == user:
                    fail_user += 1

        failure_list.append(fail_user/arrive_user)

    indices = sorted(
    range(1, len(failure_list)+1),
    key=lambda i: failure_list[i-1],
    reverse=True,
    )

    return indices

    
    # 런타임 에러
    # # stage index 리스트 만들기
    # stage_index = [ i for i in range(1, N+1) ]
    # # print(failure_list)
    # # print(stage_index)

    # # 인덱스 별 값 비교해서 인덱스 순서 바꾸기
    # for i in range(len(stage_index)):
    #     for j in range(i+1, len(stage_index)):
    #         # print(failure_list[i], failure_list[j])
    #         # print(i, j)
    #         # print(failure_list[i] < failure_list[j])
    #         if failure_list[i] < failure_list[j]:
    #             failure_list[i], failure_list[j] = failure_list[j], failure_list[i]
    #             stage_index[i], stage_index[j] = stage_index[j], stage_index[i]
    #         elif failure_list[i] == failure_list[j] and stage_index[i] > stage_index[j]:
    #             failure_list[i], failure_list[j] = failure_list[j], failure_list[i]
    #             stage_index[i], stage_index[j] = stage_index[j], stage_index[i]

    # return stage_index
            # print('중간', stage_index)


    # print('최종', stage_index)
    # a = failure_list.index(max(failure_list))
    # print(a)
        # failuser_dict[stage] = fail_user/arrive_user

a = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print(a)