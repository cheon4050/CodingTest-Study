import sys
from collections import deque

input = sys.stdin.readline

def bfs(arr, a, b, visited):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    indexArr = [(a,b)]
    total = arr[a][b]
    cnt = 1
    while q:
        x, y = q.popleft()
        for move in moves:
            dx = move[0] + x
            dy = move[1] + y
            if 0 <= dx <N and 0 <= dy < N and not visited[dx][dy] and L <= abs(arr[x][y]-arr[dx][dy]) <= R:
                visited[dx][dy] = True
                q.append((dx,dy))
                indexArr.append((dx, dy))
                total += arr[dx][dy]
                cnt += 1
    result = total//cnt
    for x, y in indexArr:
        arr[x][y] = result

N, L, R = map(int, input().split())
arr = []
cnt = 0

for _ in range(N):
    arr.append(list(map(int, input().split())))

while True:
    temp = [arr[i][:] for i in range(N)]
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(temp, i, j, visited)
    if temp == arr:
        break
    arr = [temp[i][:] for i in range(N)]
    cnt += 1

print(cnt)

