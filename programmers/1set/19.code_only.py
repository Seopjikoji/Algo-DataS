import string

def solution(s, skip, index):

    # 알파벳 리스트
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # alphabet2 = list(string.ascii_lowercase)

    # 변하는 결과값
    change = ''

    # s 순회하면서 각각의 알파벳들이 어떻게 변할지 정함
    for c in s:
        # print(c, '새로 시작')
        # 시작점(정해짐)
        start = alphabet.index(c)

        # 알파벳 순회 index(조건과 상관 없이 진행되는)
        a_index = 0

        # 알파벳 위치(for 문 내에서 index 범위까지 변화해야하는 index)
        c_index = 0

        while index > c_index:
            
            #순회할 때마다 그냥 증가(처음부터 증가하고 값 판단하는게 맞음)
            a_index += 1

            if start + a_index == 26:
                start = 0
                a_index = 0
                
            if alphabet[start + a_index] not in skip:
                c_index += 1
            # print(alphabet[start + a_index], c_index)
            
        change += alphabet[start + a_index]

    return change
            

a = solution("aukks", "wbqd", 5)
print(a)