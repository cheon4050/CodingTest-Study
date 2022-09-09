import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y, c): # dfs 탐색
    visited[x][y] = True

    for i in range(4): # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]: # 범위 내에 있고 아직 탐색하지 않은 경우
                if c == graph[nx][ny]: # 탐색하는 곳이 이전에 봤던 색이면 재귀적으로 탐색
                    dfs(nx, ny, c)


n = int(input())
graph = [list(map(str, input().strip())) for _ in range(n)] # 각 노드가 연결된 정보 저장
visited = [[False] * n for _ in range(n)] # 탐색 여부 저장
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
no = 0 # 적록색약이 아닌 사람이 보는 구역

for i in range(n): # 적록색약이 아닌 사람이 보는 구역을 dfs 탐색을 통해 찾는다
    for j in range(n):
        if not visited[i][j]: # 방문하지 않은 좌표이면 dfs로 탐색
            dfs(i, j, graph[i][j])
            no += 1

for i in range(n): # G를 R로 변경
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

yes = 0 # 적록색약인 사람이 보느 구역
visited = [[False] * n for _ in range(n)] # 탐색 여부 저장

for i in range(n): # 적록색약인 사람이 보는 구역을 dfs 탐색을 통해 찾는다
    for j in range(n):
        if not visited[i][j]: # 방문하지 않은 좌표이면 dfs로 탐색
            dfs(i, j, graph[i][j])
            yes += 1

print(no, yes)
