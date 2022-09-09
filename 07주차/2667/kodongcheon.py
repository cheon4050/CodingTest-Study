from collections import deque
N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result = []
def BFS(a, b,arr,visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    while(q):
        x, y = q.popleft()
        for i in range(4):
            move_x = x + dx[i]
            move_y = y + dy[i]
            if move_x < 0 or move_y < 0 or move_x >= len(arr) or move_y >= len(arr[0]) or visited[move_x][move_y] == True:
                continue
            if arr[move_x][move_y] == 0:
                continue
            else:
                cnt += 1
                visited[move_x][move_y] = True
                q.append((move_x, move_y))
    return cnt

for i in range(N):
    for j in range(N):
        if arr[i][j] != 0 and not visited[i][j]:
            result.append(BFS(i, j, arr, visited))
result.sort()
print(len(result))
print(*result, sep="\n")
