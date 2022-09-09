from itertools import combinations
import copy

def dfs(x, y):
    # 바이러스 걸린 구역일 때만 상하좌우 보기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 넘어가면 넘어감
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 벽 말고 빈공간일때만 전파
        if temp_graph[nx][ny] == 0:
            temp_graph[nx][ny] = 2
            dfs(nx, ny)
    return

n, m = map(int, input().split())
graph = []

wall = 0
list_empty = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            list_empty.append((i, j))

# 빈 공간에 벽을 세울 수 있는 경우의 수 전부
list_wall_combi = list(combinations(list_empty, 3))
safe = 0

for i in list_wall_combi:
    # deepcopy 안쓰면 graph의 값이 계속 바뀐다
    temp_graph = copy.deepcopy(graph)
    for j in i:
        # 벽 세움
        temp_graph[j[0]][j[1]] = 1
    for j in range(n):
        for k in range(m):
            if temp_graph[j][k] == 2:
                # 바이러스 있는 위치에서 dfs 돌림
                dfs(j, k)
    tmp_safe = 0
    for i in temp_graph:
        for j in i:
            if j == 0:
                tmp_safe += 1
    if safe < tmp_safe:
        safe = tmp_safe
print(safe)

# from collections import deque
# import copy
#
# N, M = map(int, input().split())
# lab = [list(map(int, input().split())) for _ in range(N)]
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, 1, -1]
#
# safezone = 0
#
# def spread_virus():
#     global safezone
#     lab_ = copy.deepcopy(lab)
#
#     queue = deque()
#     for i in range(N):
#         for j in range(M):
#             if lab_[i][j] == 2:
#                 queue.append((i, j))
#
#     while queue:
#         y, x = queue.popleft()
#         for i in range(4):
#             ny, nx = y+dy[i], x+dx[i]
#             if 0 <= ny < N and 0 <= nx < M:
#                 if lab_[ny][nx] == 0:
#                     lab_[ny][nx] = 2
#                     queue.append((ny, nx))
#
#     safezone = max(safezone, sum(l.count(0) for l in lab_))
#
#
# def build_wall(wall):
#     if wall == 3:
#         spread_virus()
#         return
#
#     for i in range(N):
#         for j in range(M):
#             if lab[i][j] == 0:
#                 lab[i][j] = 1
#                 build_wall(wall+1)
#                 lab[i][j] = 0
#
# build_wall(0)
# print(safezone)