def solution(survey, choices):
    print(survey, choices)

    # 점수표
    choice = [3, 2, 1, 0, 1, 2, 3]

    # 점수 결과
    score_dict = { 'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0 }
    # 순회하면서 점수 결과 만들기
    for i in range(len(survey)):
        
        # 쪼개기
        f,s = survey[i]

        if choices[i] != 4:
            if choices[i] < 4:
                score_dict[f] += choice[choices[i]-1]
            else:
                score_dict[s] += choice[choices[i]-1]

    # 뭔가 더 좋은 방법이 있을 것 같은데
    first = 'R' if score_dict['R'] >= score_dict['T'] else 'T'
    second = 'C' if score_dict['C'] >= score_dict['F'] else 'F'
    third = 'J' if score_dict['J'] >= score_dict['M'] else 'M'
    fourth = 'A' if score_dict['A'] >= score_dict['N'] else 'N'

    return f'{first}{second}{third}{fourth}'


a = solution(["TR", "RT", "TR"], [7, 1, 3])
print(a)