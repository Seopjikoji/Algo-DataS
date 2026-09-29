def solution(new_id):

    # 알파벳, 숫자 사전
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    char = ['-', '_', '.']

    # 추천 받은 아이디 변수 초기화
    rec_id = ''

    # 1단계 검증(대문자 > 소문자화, 내장 함수 바로 안떠오름, 맛았네, lower, upper 함수)
    rec_id = new_id.lower()

    # 2단계 검증(알파벳 소문자, 숫자, 뺴기, 밑줄, 마침표를 제외한 모든 문자 제거)
    # 두번째 id 생성용 변수 추가
    sec_id = ''
    for i in rec_id:
        if i in alphabet or i in num or i in char:
            sec_id += i
    rec_id = sec_id

    # 3단계 검증(. 가 .. 두 개 이상 반복되면 . 로 대체)
    # 얘도 순회하면서 해당 문자가 . 이고 다음 것도 . 이면 붙이는 식으로 해야하나 ? 앞 뒤 자르는 것보다 그냥 하나씩 더하는게 나을 듯
    # 세번째 id 생성용 변수 추가
    thd_id = ''
    for v in rec_id:
        if len(thd_id) != 0 and thd_id[-1] == '.' and v == '.':
            pass
        else:
            thd_id += v
    rec_id = thd_id    
        # if i !=0 and rec_id[i-1] == '.' and rec_id[i] == '.':
        #     rec_id = rec_id[0:i]+rec_id[i+1:len(rec_id)+1]
    # 4단계(맨앞, 맨뒤 . 제거)
    if len(rec_id) != 0 and rec_id[0] == '.':
        rec_id = rec_id[1:]

    # - 인덱스로 할 수 있는 방법은 없으려나 ??  
    if len(rec_id) != 0 and rec_id[-1] == '.':
        rec_id = rec_id[0:len(rec_id)-1]

    # 5단계(빈 문자열이면 a 로 대체)
    if rec_id == '':
        rec_id = 'a'

    # 6단계(16자 이상이면 처음부터 15까지만 남김)
    if(len(rec_id) > 15):
        rec_id = rec_id[0:15]
    
    # 한번 더 추가(문제 보기에 나와 있음)
    # - 인덱스로 할 수 있는 방법은 없으려나 ??  
    if len(rec_id) != 0 and rec_id[-1] == '.':
        rec_id = rec_id[0:len(rec_id)-1]


    # 7단계(2글자 이하면 마지막 글자를 길이가 3될 떄까지 이어붙임)
    while(len(rec_id)<3):
        rec_id += rec_id[-1]

    return rec_id

    # print(rec_id)

a = solution("abcdefghijklmn.p")
print(a)