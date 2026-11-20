def solution(participant, completion):

    # 정답
    answer = ''

    # 오름차순 배열
    participant.sort()
    completion.sort()

    # 마지막에 알파벳 아닌 문자 대입
    completion.append('0')

    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            
            # 뒤 부터는 계속 달라짐
            break

    return answer

a = solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])