def solution(s):

    # count 배열
    count = [0, 0]

    # 결과 담을 배열
    result = []

    # 초기값 초기화
    start = 0
    x = s[start]
    # 순회
    for i, value in enumerate(s):
        # print(count)
        # print(start, x)
        if x == value:
            count[0] += 1
        else:
            count[1] += 1

        if count[0] == count[1]:
            result.append(s[start:i+1])

            start = min(i + 1, len(s) - 1)
            x = s[start]

            # 초기화 범위 제한
            # if i + 1 < len(s):
            #     start = i + 1
            #     x = s[start]

            # 따로 초기화 안해도 됨, 어차피 같아지는 순간에는 멈출거고 이 상태에서 시작하면 초기화 한거랑 똑같은 효과, 다르면 계속 다르게 감
            count = [0, 0]
        
        # 마지막 index 에서 체크만 해주면 될 듯
        elif i == len(s) - 1:
            result.append(s[start:i+1])

        # print(result)

    return len(result)

a = solution("banana")
print(a)