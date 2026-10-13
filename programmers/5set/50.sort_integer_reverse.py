def solution(n):

    # 문자열로 만들고 내림차순 배열 후 다시 정수로 반환
    return int(''.join(sorted(str(n), reverse=True)))

a = solution(118372)

print(a)