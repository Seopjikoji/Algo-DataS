def solution(id_list, report, k):

    # report 결과 순회하면서 누구에게 누가 신고했는지 dict 만들기
    report_list = {}

    for i in report:
        reporter, reported = i.split(' ')
        if reported not in report_list:
            report_list[reported] = [reporter]
        else:
            if reporter not in report_list[reported]:
                report_list[reported].append(reporter)
            # report_list[reported] = list(set(report_list[reported]))

    reported_all_list = []

    # 만들어진 dict key 에 해당하는 값들을 모두 합침
    for i in report_list.values():
        if len(i) >= k:
            reported_all_list += i

    result = []

    # id_list 순회하면서 결과 값 도출
    for i in id_list:
        result.append(reported_all_list.count(i))
    
    return result

a = solution(
    ["con", "ryan"],
    ["ryan con", "ryan con", "ryan con", "ryan con"],
    3
    )

print(a)