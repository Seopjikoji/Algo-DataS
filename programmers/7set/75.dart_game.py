import re

def solution(dartResult):

    # 정답
    sum = 0

    # 이전 점수 초기화 변수
    before = 0

    # 영역별 제곱 사전
    space_dict = { 'S': 1, 'D': 2, 'T': 3 }

    parsed = re.findall(r"\d+[SDT][*#]?", dartResult)

    # 점수표
    # first = 0
    # second = 0
    # third = 0

    # print(parsed)
    # 순회하면서 값 가져오기, 일단 split을 해볼까
    for i in parsed:
        
        # 점수 초기화
        score = 0

        # 숫자 초기화
        num = ''

        for j in i:
            if j.isdigit():
                num += j
            elif j in ['S', 'D', 'T']:
                score = int(num) ** space_dict[j]
            else:
                if j == '*':
                    before *= 2
                    score *= 2
                else:
                    score *= -1
        print(score)
        sum += score
        before = score

    return sum    

    # for i in dartResult:
        # if int(i) = int:


a = solution('1S2D*3T')
print(a)