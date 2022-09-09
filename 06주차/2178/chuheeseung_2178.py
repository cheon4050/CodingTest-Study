from collections import deque

n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, input())))

dx = [-1, 0, 1, 0] # 탐색 상하좌우로 해야 해서 방향 설정
dy = [0, -1, 0, 1]

visited = [[0] * m for _ in range(n)]

q = deque([(0, 0)])
visited[0][0] = 1 # 첫번째 위치가 주어짐 -> 1로 변경

while q:
    x, y = q.popleft()

    if x == n - 1 and y == m - 1: # 미로가 끝에 도달했을 때 해당 값을 호출
        print(visited[x][y])

    for i in range(4): # 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m: # 미로 범위 안에 있는 경우
            if visited[nx][ny] == 0 and maze[nx][ny] == 1: # 아직 탐색 안했는데 이동할 수 있는 칸이면
                visited[nx][ny] = visited[x][y] + 1 # visited 배열에 추가해줌
                q.append((nx, ny)) # 큐에 추가해준다


