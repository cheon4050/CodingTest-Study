from collections import defaultdict
from collections import deque

N, M = map(int, input().split())
step = defaultdict(list)    # 그래프 연결 정보
in_degree = [0] * (N + 1)   # 진입 차수
q = deque()
result = []

for i in range(M):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]):
        step[temp[j]].append(temp[j+1])
        in_degree[temp[j+1]] += 1

for i in range(1, N + 1):  # 진입 차수가 0 인 정점을 모두 큐에 삽입
    if in_degree[i] == 0:
        q.append(i)

while q:
    n = q.popleft()
    result.append(n)

    for v in step[n]:
        in_degree[v] -= 1   # 이웃 노드 탐색 하면서 진입 차수 갱신
        if in_degree[v] == 0:  # 진입 차수가 0이라면 큐에 추가
            q.append(v)

if len(result) != N:       # 모든 노드를 방문하기 전에 큐가 빈다면 사이클이 존재
    print(0)
else:
    for n in result:
        print(n)