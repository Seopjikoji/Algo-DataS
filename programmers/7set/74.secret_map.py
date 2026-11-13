def binary_converter(n, num):
    result = ''
    
    # 몫
    while num:
        # 앞에 이어 붙임
        result = str(num % 2) + result
        num //= 2
        if num == 1:
            result = '1' + result
            break
    
    # 길이 다르면 공백 처리
    if len(result) != n:
        result = '0'*(n-len(result)) + result
    return result

def solution(n, arr1, arr2):

    # 결과 변수 초기화
    result = []

    # 2진수 변환기(숫자 입력시 공백 포함해서 만듦)

    # 배열 순환하면서 2진수로 바꾸고 비교
    for i in range(0, n):
        first_binary = binary_converter(n, arr1[i])
        second_binary = binary_converter(n, arr2[i])
        mid_result = ''
        for j in range(0, n):
            if first_binary[j] == '0' and second_binary[j] == '0':
                mid_result += ' '
            else:
                mid_result += '#'
        result.append(mid_result)

    # print(result)
            
    return result

a = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
print(a)
# binary_converter(5, 0)
