def solution(keymap, targets):

    # target 알파벳
    target = []
    # target 알파벳 찾기
    for i in targets:
        for j in i:
            target.append(j)

    rm_dup_target = set(target)
    

    # target 별 최소 클릭 사전 만들기
    # 0으로 초기화 후 사전 keymap 순회
    count_dict = { i: 0 for i in rm_dup_target }
    print(count_dict)

    for i in keymap:
        for j, value in enumerate(i):
            for k in rm_dup_target:
                if k == value:
                    if count_dict[k] == 0:
                        count_dict[k] = j + 1
                    else:
                        count_dict[k] = min(count_dict[k], j + 1)

    # print(count_dict)
    # 최소 횟수 집계 배열
    min_list = []

    for i in targets:
        # 최소 횟수
        min_count = 0
        # print(i)
        for j in i:
            if count_dict[j] == 0:
                min_count = - 1
                break
            else:
                min_count += count_dict[j]
        min_list.append(min_count)

    return min_list

a = solution(["AA"], ["B"])
print(a)