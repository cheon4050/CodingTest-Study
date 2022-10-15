import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n : 가수의 개수, m : 보조 pd의 개수
indegree = [0] * n
result = [1] * n
graph = [[] for i in range(n)]

for _ in range(m):
    list_ = list(map(int, input().split()))
    for a, b in zip(list_[1:], list_[2:]): # Q. 왜 이렇게 자르는지 모르겠다
        graph[a-1].append(b - 1)
        indegree[b-1] += 1 # 진입 차수

# 위상 정렬
result = []
q = deque()

for i in range(n): # 진입 차수가 0인 노드를 큐에 넣는다 (진입 차수가 0인 노드가 시작하는 노드니까)
    if indegree[i] == 0:
        q.append(i)

while q: # 큐가 빌때까지 while문 반복
    now = q.popleft() # 큐에서 하나 꺼내서 해당 노드에서 나가는 간선을 그래프에서 제거
    result.append(now + 1) # 결과 추가

    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0: # 새롭게 진입 차수가 0인 노드를 다시 큐에 넣는다
            q.append(i)

if sum(indegree) > 0: # 순서 정하는게 불가능한 경우
    print(0)
else:
    [print(i) for i in result]