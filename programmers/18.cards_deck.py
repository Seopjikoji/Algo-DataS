def solution(cards1, cards2, goal):

    # 사용할 수 있는 카드 뭉치 각각의 인덱스 변화
    cards1_index = 0
    cards2_index = 0

    # 카드 뭉치의 각각 길이
    card1_len = len(cards1)
    card2_len = len(cards2)

    # goal 순회하면서 만들 수 있는 단어인가 체크, 카드 덱 순서대로 이동
    for g in goal:
        if cards1_index < card1_len and cards1[cards1_index] == g:
            cards1_index += 1
            
        elif cards2_index < card2_len and cards2[cards2_index] == g:
            cards2_index += 1
        else:
            return 'No'
    return 'Yes'    
        

a = solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])

print(a)
