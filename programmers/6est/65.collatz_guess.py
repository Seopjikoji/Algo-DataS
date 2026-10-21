def solution(num):

    # 반복되는 횟수 변수 초기화
    repeat_count = 0

    while repeat_count < 500:
        if num == 1:
            return 0
        
        # 짝수인 경우
        if num % 2 == 0:
            num /= 2
        # 홀수인 경우
        else:
            num = (num * 3) + 1

        # 콜라츠 추측 실행 횟수 1회 추가
        repeat_count += 1

        if num == 1:
            return repeat_count

    if repeat_count == 500:
        return -1

a = solution(6)
print(a)