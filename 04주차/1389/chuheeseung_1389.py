from collections import deque
import sys

input = sys.stdin.readline

def bfs(x):
    visited = [0] * (n + 1) # 함수가 호출될 때 마다 리스트이 값들을 모두 0으로 초기화
    sum = 0 # 케빈베이컨수 저장할 변수
    queue = deque()
    queue.append(x) # 인자로 받은 수 x를 큐에 집어넣는다

    while queue: # 큐가 비어있지 않으면
        q = queue.popleft() # 선입선출로 큐에서 하나 뽑아서 변수에 저장

        for i in graph[q]: # 변수를 인덱스로
            if visited[i] == 0 and i != q: # 해당 값 방문한 적 없고 i가 q와 같지 않은 조건 만족하면
                visited[i] = visited[q] + 1 # 이전 값에 1 더해서 visited에 저장
                queue.append(i) # i를 큐에 추가

    visited[x] = 0 # 큐가 비어서 while문이 끝나면 함수의 인자로 전달받은 수를 index로 하는 값을 0으로 만든다
                   # 자기 자신과 친구 못하게

    for i in range(len(visited)): # 케빈베이컨수 합 구해서 변수에 넣어준다
        sum += int(visited[i])

    result[x] = sum

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
result = [0] * (n + 1)
indexRange = 101 # 사람 수 최대 100명
valueRange = 5001 # 관계 수 최대 5000

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1): # 1 ~ n+1까지의 수를 bfs 함수의 인자로 호출
    bfs(i)

for i in range(1, n + 1):
    if result[i] < valueRange:
        indexRange = i
        valueRange = result[i]

print(indexRange)