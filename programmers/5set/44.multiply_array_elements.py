def solution(a, b):

    # 합 초기 변수
    sum = 0

    # 길이 같으니까, enumerate 로 한 배열 순회하면서 index 랑 value 곱해서 더하면 될 듯
    for index, value in enumerate(a):
        sum += value * b[index]

    return sum

a = solution([-1,0,1], [1,0,-1])
print(a)