def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    #신고 횟수 계산
    for r in set(report):
        reports[r.split()[1]] += 1
    #신고 횟수 k개 넘은 갯수 계산
    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer