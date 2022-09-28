import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
inDegree = [0 for i in range(32001)]
graph = [[] for i in range(32001)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])

for a, b in arr:
    inDegree[b] += 1 # 더 큰 학생 b의 차수 + 1
    graph[a].append(b) # a가 b를 참조한다고 생각

for i in range(1, n + 1):
    if inDegree[i] == 0: # 차수가 0인 경우에 큐에 추가
        queue.append(i)

while queue: # 큐에 원소가 있을 때까지 반복
    student = queue.popleft() # 큐에서 원소를 꺼냄

    for j in graph[student]:
        inDegree[j] -= 1 # 꺼낸 원소와 연결된 간선 제거
        if inDegree[j] == 0: # 제거한 후에 진입 차수가 0인 정점을 큐에 추가
            queue.append(j)
    print(student, end = ' ')