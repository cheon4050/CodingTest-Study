from collections import deque
N, M = map(int, input().strip().split())

# 맵의 행 * 맵의 열 * 벽(부수지 않고 이동할 경우, 부순 후 이동할 경우)
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

# 주어진 입력 맵 넣기
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

# 한 칸에서 이동 가능한 상하좌우의 경우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 시작하는 칸이 바로 끝나는 칸일 경우
if N == 1 and M == 1 and graph[0][0] == 0:
    # 최단 거리 1 출력
    print(1)
else:
    visited[0][0][0] = 1
    queue.append([0, 0, 0])

    flag = 0
    while queue:
        x, y, z = queue.popleft()

        # 상하좌우로 이동한 모든 경우
        # (queue에 넣고 비교 - BFS)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 상하좌우로 이동한 경우에 범위 내에 있음
            if 0 <= nx < N and 0 <= ny < M and visited[z][nx][ny] == 0:

                # 벽이고 벽을 부수지 않은 경우
                if graph[nx][ny] == 1 and z == 0:
                    visited[1][nx][ny] = visited[0][x][y] + 1
                    queue.append([nx, ny, 1])

                # 벽이 아니라 벽을 부수지 않고 갈 경우
                elif graph[nx][ny] == 0:
                    visited[z][nx][ny] = visited[z][x][y] + 1
                    queue.append([nx, ny, z])

                # 끝나는 칸에 도달한 경우
                if nx == N - 1 and ny == M - 1:
                    print(visited[z][nx][ny])
                    flag = 1
                    break

        if flag == 1:
            break

    if flag == 0:
        print(-1)