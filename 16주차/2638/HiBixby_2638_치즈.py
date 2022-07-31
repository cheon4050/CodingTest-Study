from collections import deque


def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(0 <= nx < n and 0 <= ny < m and not visited[nx][ny]):
                if paper[nx][ny] >= 1:
                    paper[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


n, m = map(int, input().split())
paper = [list(map(int, input().split()))for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hours = 0
while True:
    visited = [[False for _ in range(m)]for _ in range(n)]
    bfs()
    is_melt_in_this_round = False
    for i in range(n):
        for j in range(m):
            if paper[i][j] >= 3:
                paper[i][j] = 0
                is_melt_in_this_round = True
            elif paper[i][j] == 2:
                paper[i][j] = 1
    if is_melt_in_this_round:
        hours += 1
    else:
        break
print(hours)
