import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001

n, k = map(int, input().split())
q = deque()
q.append(n)
visited = [-1 for _ in range(MAX)]
visited[n] = 0

while q:
    s = q.popleft()

    if s == k:
        print(visited[s])
        break

    if 0 <= s-1 < MAX and visited[s-1] == -1: # x-1 이동
        visited[s-1] = visited[s] + 1 # 방문시 +1 추가
        q.append(s-1)
    if 0 <= s*2 < MAX and visited[s*2] == -1:
        visited[s*2] = visited[s] # 순간이동은 0초 걸려서 +1 안함
        q.appendleft(s*2) # left로 가장 맨 앞으로 넘겨준다
    if 0< s+1 < MAX and visited[s+1] == -1: # x+1 이동
        visited[s+1] = visited[s] + 1 # 방문시 +1 추가
        q.append(s+1)