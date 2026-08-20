def solution(cards1, cards2, goal):

    # 사용할 수 있는 카드 뭉치 각각의 인덱스 변화
    cards1_index = 0
    cards2_index = 0

    # goal 순회하면서 만들 수 있는 단어인가 체크, 카드 덱 순서대로 이동
    for g in goal:
        if cards1[cards1_index] == g:
            # print(cards1_index, '1')
            if cards1_index < len(cards1) - 1:
                cards1_index += 1
            
        elif cards2[cards2_index] == g:
            if cards2_index < len(cards2) - 1 :
                cards2_index += 1
        else:
            return 'No'

    return 'Yes'    
        

a = solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])

print(a)
