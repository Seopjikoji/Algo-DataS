def solution(left, right):

    # 정답 변수
    sum = 0

    # 제곱근 기호?
    # ^ 비트 연산자임
    # ** 0.5, ** 제곱 기호

    # 범위 순회
    # 최대 1000 * 1000 이라서 시간 복잡도 허용 가능

    for i in range(left, right+1):
        # 약수 개수 초기화
        divisor_count = 0
        
        for j in range(1, i+1):
            if i % j == 0:
                divisor_count += 1

        # 다른 풀이, 수학적 센스 필요        
        # for j in range(1, int((i)**0.5)+1):
        #     if i % j == 0:
        #         divisor_count += 1
        #         if i // j != j:
        #             divisor_count += 1

        if divisor_count % 2 == 0:
            sum += i
        else:
            sum -= i

    return sum        

a = solution(24, 27)
print(a)