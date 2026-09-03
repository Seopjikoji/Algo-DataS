def solution(ingredient):

    # 스택으로 풀기
    stack = []
    # 햄버거 개수
    count = 0

    for i in ingredient:
        stack.append(i)
        # print(stack)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            count += 1
            del stack[-4:]

    return count
    # 햄버거 개수
    # count = 0

    # 멈춤 여부
    # stop = False

    # 순회하면서 조건 맞는 배열 찾기(시간 초과)
    # while not stop:
    #     for i in range(len(ingredient)):
    #         if ingredient[i:i + 4] == [1, 2, 3, 1]:
    #             count += 1
    #             del ingredient[i:i + 4]
    #             stop = False
    #             break
    #         else:
    #             stop = True
    # stack = []
    # count = 0
    # for i in ingredient:
    #     stack.append(i)
    #     if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
    #         count += 1
    #         for _ in range(4):
    #             stack.pop()
    # print(ingredient)

a = solution([2, 1, 1, 2, 3, 1, 2, 3, 1])
print(a)