def solution(id_list, report, k):
    r,a,ban=[],[],set()
    d={id:set() for id in id_list}
    for e in set(report):
        tmp=e.split()
        d[tmp[0]].add(tmp[1])
        r.append(tmp[1])
    for id in id_list:
        if r.count(id)>=k:
            ban.add(id)
    for id in id_list:
        a.append(len(d[id]&ban))
    return a

id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k=2
print('answer is:',solution(id_list,report,k))