def solution(t, p):

    # 슬라이싱한 문자보다 p가 크거나 같은 경우 count
    count = 0

    # 기준 문자 길이
    t_len = len(t)

    # 비교(부분) 문자 길이
    p_len = len(p)

    # 기준 문자열 슬라이싱 하면서 크기 비교
    for i in range(0, t_len - p_len + 1):
        # print(t[i : i + p_len])
        if t[i : i + p_len] <= p:
            count+=1

    return count

a = solution("3141592", "271")
print(a)