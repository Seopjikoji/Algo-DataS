def change_date_by_term(date, month):
    # y, m, d = date.split(int, '.')
    y, m, d = map(int, date.split('.'))

    # add_y = month // 12
    # add_m = month % 12

    total_m = m + month
    if total_m % 12 == 0:
        y += (total_m // 12) - 1
        m = 12 
    else:
        y += (total_m // 12)
        m = (total_m % 12)
    # print(m)
    # print(month)
    # print(total_m)

    # y += (total_m // 12)
    # m = (total_m % 12)

    # y += (m - 1) // 12
    # m = m % 12

    result = f"{y}.{m:02d}.{d:02d}"
    return result


def solution(today, terms, privacies):

    # 결과 담을 리스트, 어차피 개인정보 인덱스 작은 것부터 순회할거라서 그냥 append 만 하면 될 듯. 처음부터 순회하니깐
    result = []

    # 약관 dict(약관명 중복 X)
    terms_dict = {}

    for i in terms:
        term, month = i.split()
        terms_dict[term] = int(month)

    # 개인정보 순회하면서 수집일자 + 약관별 달 수 < today 인지 아닌지 판단하고, 아니면 result 에 통합
    for index, p in enumerate(privacies):
        date, term = p.split()
        print(change_date_by_term(date, terms_dict[term]), today)
        if change_date_by_term(date, terms_dict[term]) <= today:
            result.append(index + 1)

    return result         

a = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
print(a)