from collections import deque

n, m = map(int, input().split())

map = [list(map(int, input().rstrip().split())) for _ in range(n)]
answer = [[0] * m for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

def bfs(point):
    queue = deque()
    queue.append(point)
    visited = set()
    visited.add(point)
    while queue:
        x, y = queue.popleft()
        for way in range(4):
            xx, yy = x + dx[way], y + dy[way]
            if (xx < 0) or (xx >= n) or (yy < 0) or (yy >= m) or ((xx, yy) in visited):
                continue
            if map[xx][yy] == 0:
                continue
            if map[xx][yy] == 1:
                answer[xx][yy] = answer[x][y] + 1
                queue.append([xx, yy])
                visited.add((xx, yy))
    return answer, visited

def final_point(): #2는 목표지점
    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                return (i, j)

def compare_zero(): # 0유무 갈수있는길인지 아닌지 구분
    c = set()
    for i in range(n):
        for j in range(m):
            if map[i][j] != 0:
                c.add((i, j))
    return c

def early_v(point_set):
    for i in point_set:
        x, y = i
        answer[x][y] = -1
    return answer

f_point = final_point()
flag = compare_zero()

answer, v = bfs(f_point)

remain = flag - v # 남아있는 것 중에서 후처리?
if len(remain) != 0:
    answer = early_v(remain)

for x in answer:
    print(" ".join(map(str, x)))
    
    # 런타임 에러ㅠㅠ