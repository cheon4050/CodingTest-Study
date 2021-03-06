from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0, 0, 1])

    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # 방문 여부 체크 배열
    visited[0][0][1] = 1
    # visited[][][0] : 벽을 한번 부순 상태, visited[][][1] : 벽을 부술 수 있는 상태

    while q: # 큐가 빌 때까지 반복
        x, y, c = q.popleft() # 좌표, 벽을 부술 수 있는 남은 횟수

        if x == n - 1 and y == m - 1: # 도착 위치에 오면 최단거리 횟수 반환
            return visited[x][y][c]

        for i in range(4):
            tx = dx[i] + x
            ty = dy[i] + y

            if 0 <= tx < n and 0 <= ty < m:
                # 벽을 만나고 벽을 한번 부술 수 있는 경우
                if a[tx][ty] == '1' and c == 1: # 벽을 뚫을 수 있고 벽을 만나면 + 1
                    visited[tx][ty][0] = visited[x][y][1] + 1
                    q.append([tx, ty, 0]) # c를 -1 해서 저장
                # 벽이 없고 방문한 적이 없는 경우
                elif a[tx][ty] == '0' and visited[tx][ty][c] == 0:
                    visited[tx][ty][c] = visited[x][y][c] + 1 # 아직 방문 안했고 벽이 아니면 + 1
                    q.append([tx, ty, c])

    return -1;

n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(list(input()))

print(bfs())