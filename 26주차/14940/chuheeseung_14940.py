from collections import deque

n, m = map(int, input().rstrip().split())
box = [0 for _ in range(n)]
tr, tc = 0, 0  # 목표지점

ans = [[-1 for _ in range(m)] for _ in range(n)] # 답을 출력할 리스트, 방문 할 수 없는 곳은 -1

v = [[False for _ in range(m)] for _ in range(n)] # 방문 리스트
q = deque([[tr, tc, 0]]) # BFS
ans[tr][tc] = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    box[i] = list(map(int, input().rstrip().split()))
    for j in range(len(box[i])):
        if box[i][j] == 2: # 목표지점 저장
            tr, tc = i, j

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            ans[i][j] = 0 # 원래 갈 수 없는 땅인 위치는 0으로 고정

while q: # BFS 탐색
    t = q.popleft()
    cr, cc, cnt = t[0], t[1], t[2]
    if v[cr][cc]:
        continue
    v[cr][cc] = True
    for d in range(4):
        nr = cr + dx[d]
        nc = cc + dy[d]
        if 0 <= nr < n and 0 <= nc < m and not v[nr][nc]:
            if box[nr][nc] == 1:
                ans[nr][nc] = cnt + 1
                q.append([nr, nc, cnt + 1])

# 출력
for i in range(n):
    print(*ans[i])