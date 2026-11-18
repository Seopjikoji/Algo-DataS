import re

def solution(dartResult):

    # 이전 점수 초기화 변수
    before = 0

    # 영역별 제곱 사전
    space_dict = { 'S': 1, 'D': 2, 'T': 3 }

    parsed = re.findall(r"\d+[SDT][*#]?", dartResult)

    # 점수표
    score_list = [0, 0, 0]

    # print(parsed)

    # 순회하면서 값 가져오기, 일단 split을 해볼까
    for index, i in enumerate(parsed):
        
        # 숫자 초기화
        num = ''

        # 점수 초기화
        score = 0

        for value in i:
            if value.isdigit():
                num += value
            elif value in ['S', 'D', 'T']:
                score = int(num) ** space_dict[value]
            else:
                # 옵션 적용
                if value == '*':
                    # before *= 2
                    score *= 2
                    if index != 0:
                        before = score_list[index-1] * 2
                        score_list[index-1] = before
                else:
                    score *= -1
            score_list[index] = score

    return sum(score_list)    

a = solution('1S*2T*3S')
print(a)