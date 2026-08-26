def solution(s):

    # 결과 리스트
    result_list = []

    # 최근 인덱스 사전
    recent_character_index_dict = {}

    # 문자열 순회하면서 인덱스 사전 체크(처음 나온 애는 -1, 인덱스 저장, 이후에 사전에 있는데 나온 원소는 본인 인덱스랑, 기존 인덱스 차이 결과에 통합하고, ㅑndex 변경해주기)
    for index, c in enumerate(s):
        if c not in recent_character_index_dict:
            result_list.append(-1)
            recent_character_index_dict[c] = index
        else:
            result_list.append(index - recent_character_index_dict[c])
            recent_character_index_dict[c] = index

    return result_list

a = solution("foobar")
print(a)