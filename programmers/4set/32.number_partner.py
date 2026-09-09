from collections import Counter

def solution(X, Y):

    # 라이브러리 활용하기
    count = Counter(X) & Counter(Y)
    
    result = ''.join(sorted(count.elements(), reverse=True))
    if len(result):
        if result[0] == '0':
            return '0'
        else:
            return result
    else:
        return '-1'
    
    # # 순회하면서 X 내 숫자 각각의 개수를 기록하는 dict 를 만든다
    # count = {}

    # # 겹치는 결과 list
    # result = [] 

    # for x in X:
    #     if x in count:
    #         count[x] += 1
    #     else:
    #         count[x] = 1

    # # print(count)

    # for y in Y:
    #     if y in count and count[y] > 0:
    #         result.append(y)
    #         count[y] -= 1

    # result = sorted(result, reverse=True)

    # if len(result) != 0:
    #     if result[0] == '0':
    #         return '0'
    #     else:
    #         return ''.join(result)
    # else:
    #     return '-1'

    
    # 시간 초과
    # # 둘이 일치하는 숫자 담은 리스트
    # result = []

    # # X 기준으로 순회하면서 일치하는
    # for target in X:

    #     i = Y.find(target)
    #     if i != -1:
    #         Y = Y[:i] + Y[i+1:]
    #         # print(Y)
    #         result.append(target)

    # result = sorted(result, reverse=True)

    # if len(result):
    #     return str(int(''.join(result)))
    # else:
    #     return '-1'


a = solution('100', '2345')
print(a)