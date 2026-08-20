def solution(keymap, targets):

    keymap_dict = {}
    # keymap 사전 만들기
    # 아 처음 찾는 인덱스만(not in 으로 처음인지 아닌지 구분)
    # 기준이 되는 정보가 있으면 그냥 얘를 먼저 만들어 놓고 생각하는게 빠름
    for i in keymap:
        for index, value in enumerate(i):
            if value not in keymap_dict:
                keymap_dict[value] = index + 1
            else:
                keymap_dict[value] = min(keymap_dict[value], index + 1)
                # if keymap_dict[value] > index + 1:
                #     keymap_dict[value] = index + 1

    # 최소 횟수 집계 배열
    min_list = []

    # 순회하면서 target 별로 계산해서 값 도출, 최소 횟수 도출하지 못할 경우 -1로 return
    for target in targets:

        min_count = 0

        for a in target:
            if a not in keymap_dict:
                min_count = -1
                break
            else:
                min_count += keymap_dict[a]
        min_list.append(min_count)

    return min_list

a = solution(["ABACD", "BCEFD"], ["ABCD","AABB"])
print(a)