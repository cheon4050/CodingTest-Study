import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())
temp = []
for _ in range(N):
    temp.append(list(map(int, input().split())))


def check(visited, arr, start):
    visited[start[0]][start[1]] = True
    q = deque([start])
    cheese = [start]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while(q):
        x, y = q.popleft()
        for move in moves:
            dx = x+move[0]
            dy = y+move[1]
            if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy] and arr[dx][dy] == 0:
                cheese.append((dx, dy))
                visited[dx][dy] = True
                q.append((dx, dy))
    if not (N-1, M-1) in cheese:
        for i, j in cheese:
            arr[i][j] = 1
cnt =0

while True:
    arr = [i[:] for i in temp]
    update = []
    visited = [[False] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and not arr[i][j]:
                check(visited, arr, [i, j])
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and arr[i+1][j] + arr[i-1][j] + arr[i][j-1] + arr[i][j+1] <= 2:
                update.append((i, j))
    if update:
        cnt += 1
        for i, j in update:
            temp[i][j] = 0
    else:
        break

print(cnt)