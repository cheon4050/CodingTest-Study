import sys
from collections import deque
input = sys.stdin.readline

def BFS(a, b, visited, arr):
    visited[a][b] = 1
    q = deque()
    q.append((a,b))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y = q.popleft()
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if temp_x < 0 or temp_y < 0 or temp_x >= len(visited) or temp_y >= len(visited[0]) or arr[temp_x][temp_y] == 0 or visited[temp_x][temp_y] != 10000:
                continue
            else:
                q.append((temp_x,temp_y))
                visited[temp_x][temp_y] = min(visited[x][y]+1, visited[temp_x][temp_y])

N, M = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(map(int, list(input().rstrip())))
    arr.append(temp)

visited = [[10000] * M for _ in range(N)]
BFS(0,0,visited, arr)
print(visited[N-1][M-1])