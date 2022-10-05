import sys
from collections import deque
input = sys.stdin.readline

# 도시 개수 n, 도로 개수 m, 거리 정보 k, 출발 도시 번호 x
# x에서 출발해서 거리가 k인 모든 도시를 구하는 프로그램
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer = [-1] * (n + 1) # -1로 초기화
answer[x] = 0 # 출발 도시의 최단 거리는 항상 0

for _ in range(m):
    a, b = list(map(int, input().split())) # 그래프를 입력받는다
    graph[a].append(b) # a -> b

q = deque([x]) # 큐에 시작점 x를 넣어주고 bfs 탐색
while q:
    now = q.popleft()

    for next in graph[now]: # now와 연결된 도시 next에 대해서 for문 반복
        if answer[next] == -1:
            # 아직 방문 안했으면 지금까지 거리(answer[now])에 + 1 값을 저장
            answer[next] = answer[now] + 1
            q.append(next) # q에 추가해서 다음 탐색할 곳으로 저장

for i in range(n + 1): # k인 곳만 찾아서 출력
    if answer[i] == k:
        print(i)

if k not in answer:
    print(-1)