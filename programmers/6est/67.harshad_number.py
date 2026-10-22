def solution(x):

    sum = 0 

    # x를 자릿수 별로 나눠서 더하기
    for i in str(x):
        sum += int(i)

    if x % sum == 0:
        return True

    return False

a = solution(13)
print(a)