from collections import defaultdict

def solution(id_list, report, k):
    answer = list() # 배열로 반환하라니까 리스트로 선언
    count = defaultdict(int) # 신고한 횟수
    user = defaultdict(set) # 신고 리스트

    for r in report: # 누가 누구를 신고했는지 딕셔너리에 담고 신고 당한 횟수를 세기
        a, b = r.split() # a가 b를 신고함

        if b not in user[a]: # 같은 사람이 1번 이상 신고 못함
            user[a].add(b)
            count[b] += 1 # 신고당한 횟수

    for id in id_list: # 이용자별로 자신이 신고한 사람이 k번 이상이면 처리된 횟수 ++
        result = 0

        for u in user[id]:
            if count[u] >= k:
                result += 1

        answer.append(result)

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
               2))

print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"],
               3))