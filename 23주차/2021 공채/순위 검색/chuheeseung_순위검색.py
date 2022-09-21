from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []
    infos = defaultdict(list)

    for i in info: # info를 조회해서 정보를 딕셔너리로 만든다
        conditions = i.split()[:-1] # info에서 조건을 분리해서 conditions에 저장
        score = int(i.split()[-1]) # info에서 점수만 분리해서 score에 저장

        for r in range(5):
            combis = list(combinations(range(4), r)) # 하나의 info에서  '-'로 바꾸는 경우의 수 16개 만들기

            for c in combis: # 각 경우에 대해서 '-'로 바꾼 가능한 조합들을 만들어서 저장
                test_cases = conditions[:]
                for v in c:
                    test_cases[v] = '-'
                infos['_'.join(test_cases)].append(score)
                # 조건이 key, 점수가 value -> 점수를 만족하는 지원자를 딕셔너리에 저장

    for item in infos:
        infos[item].sort() # value인 점수들을 오름차순으로 정렬

    for q in query: # 쿼리 돌면서 조건별로 조회
        q = q.replace('and', '').split() # 문자 제거
        conditions = '_'.join(q[:-1]) # 쿼리도 마찬가지로 분리
        score = int(q[-1])

        if conditions in list(infos): # 주어진 조건이 딕셔너리의 key로 존재하는 경우
            data = infos[conditions]

            if len(data) > 0:
                # lower bound 알고리즘으로 인덱스를 찾음
                # lower bound : 정렬된 배열에서 찾고자 하는 값 이상의 값이 처음 나타나는 위치를 찾는 알고리즘
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start) # 해당 인덱스~끝가지의 개수인 만족하는 사람 수를 answer에 저장
        else:
                answer.append(0) # 만족하는 사람이 없으면 0을 저장

    return answer

# solution(["java backend junior pizza 150","python frontend senior chicken 210",
# "python frontend senior chicken 150","cpp backend senior pizza 260",
# "java backend junior chicken 80",
# "python backend senior chicken 50"],
#          ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200",
# "cpp and - and senior and pizza 250",
# "- and backend and senior and - 150",
# "- and - and - and chicken 100","- and - and - and - 150"])