from collections import deque
T = int(input())
def BFS(arr, x, y, visited):
    if visited[x][y] == True or arr[x][y] == 0:
        return 0
    queue = deque()
    queue.append((x,y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx == len(visited) or ny == len(visited[0]) or arr[nx][ny] == 0 or visited[nx][ny] == True:
                continue
            visited[nx][ny] = True
            queue.append((nx,ny))
    return 1

for _ in range(T):
    M, N, K = map(int,input().split())
    arr = [[0]*M for i in range(N)]
    visited = [[False] * M for i in range(N)]
    cnt = 0
    for o in range(K):
        j, i = map(int,input().split())
        arr[i][j] = 1
    for i in range(N):
        for j in range(M):
            cnt += BFS(arr, i, j, visited)
    print(cnt)