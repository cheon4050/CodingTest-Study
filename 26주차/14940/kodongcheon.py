import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int, input().split()))for i in range(N)]
q = deque()
visited = [[0]* M for i in range(N)]
start = (0, 0)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            start = (i, j)
            q.append((i, j, 0))
            visited[i][j] = -1
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    x, y, cnt = q.popleft()
    for move in moves:
        dx = x+move[0]
        dy = y+move[1]
        if 0<= dx < N and 0<= dy < M and arr[dx][dy] and not visited[dx][dy]:
            visited[dx][dy] = cnt+1
            q.append((dx, dy, cnt+1))
visited[start[0]][start[1]] = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = -1

for i in visited:
    for j in i:
        print(j, end= " ")
    print()
