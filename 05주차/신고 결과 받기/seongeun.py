def solution(id_list, report, k):
    # 신고 당한 횟수
    c = {}
    # 신고한 id
    a = {}

    for i in id_list:
        c[i] = 0
        a[i] = [] #신고한 id

    for r in set(report):
        #x가 y를 신고
        x, y = r.split()
        c[y] += 1 #c[id]=id가 신고당한 횟수
        a[x].append(y)
    #각 id가 신고한 id a[id] 의 요소들 x 중 신고당한 횟수 c[x] 가 기준값 k를 넘는 요소 x의 수를 반환
    return [sum(1 if c[t] >= k else 0 for t in a[i]) for i in id_list]

print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))