import sys
input = sys.stdin.readline

r, c = map(int, input().split()) # 가로 r, 세로 c
graph = [list(map(str, input().strip())) for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
count = 1 # 말이 지나는 칸 개수

def bfs():
    global count
    queue = set([(0, 0, graph[0][0])]) # 중복되는 곳을 제거하기 위해 set

    while queue:
        x, y, z = queue.pop()
        count = max(count, len(z)) # 말이 지날 수 있는 최대 칸 초기화

        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in z:
                # 범위 내에 있고 알파벳이 중복되지 않는다면 탐색
                queue.add((nx, ny, graph[nx][ny] + z))

bfs()
print(count)