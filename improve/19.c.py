import string

def solution(s, skip, index):

    # 알파벳 리스트(내장 함수를 사용하면 간단하게 표현할 수 있음)
    # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet = list(string.ascii_lowercase)

    # 문자열을 배번 순회하면서 찾지 않고, 그냥 딱 찾음
    skip_set = set(skip)

    # 변하는 결과값(직관적으로 change > answer 로 변수명 변경)
    answer = ''

    # s 순회하면서 각각의 알파벳들이 어떻게 변할지 정함
    for c in s:
        # 시작점(정해짐)
        start = alphabet.index(c)

        # 알파벳 순회 index(조건과 상관 없이 진행되는, a_index > step 으로 직관적으로 변경)
        step = 0

        # 알파벳 위치(for 문 내에서 index 범위까지 변화해야하는 index, c_index > move_count 로 변수명 변경)
        move_count = 0

        while index > move_count:
            
            #순회할 때마다 그냥 증가(처음부터 증가하고 값 판단하는게 맞음)
            step += 1

            # 아예 변수명 하나 만듦
            next_index = (start + step) % 26

            # 생략 가능, 뭔가 그냥 앞으로 돌아온다 하면은 % 이용해서 값 변화하는 방법 생각 !
            # if start + a_index == 26:
            #     start = 0
            #     a_index = 0
                
            if alphabet[next_index] not in skip_set:
                move_count += 1
            # print(alphabet[start + a_index], c_index)
            
        answer += alphabet[(start + step) % 26]

    return answer
            

a = solution("aukks", "wbqd", 5)
print(a)