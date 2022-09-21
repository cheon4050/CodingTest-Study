from collections import deque

def solution(board, r, c):
    result = []
    q = []
    visited = [[100] * 4 for i in range(4)]
    bfs((r, c, 0), board, visited)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                q.append((i, j))
    for i, j in q:
        cnt = visited[i][j]
        dfs(i, j, [board[i][:] for i in range(4)], cnt, q[:], result)
    result = min(result)
    return result


def dfs(i, j, board, cnt, q, result):
    visited = [[100] * 4 for i in range(4)]
    targetX, targetY = bfs((i, j, 0), board, visited)
    cnt += visited[targetX][targetY] + 2
    q.pop(q.index((i, j)))
    q.pop(q.index((targetX, targetY)))
    board[i][j] = 0
    board[targetX][targetY] = 0
    if not q:
        result.append(cnt)
        return
    visited = [[100] * 4 for i in range(4)]
    bfs((targetX, targetY, 0), [board[i][:] for i in range(4)], visited)
    for i, j in q:
        dfs(i, j, [board[i][:] for i in range(4)], cnt + visited[i][j], q[:], result)


def bfs(v, arr, visited):
    q = deque([v])
    visited[v[0]][v[1]] = v[2]
    target = arr[v[0]][v[1]]
    targetX = 0
    targetY = 0
    for i in range(4):
        for j in range(4):
            if arr[i][j] == target and (i != v[0] or j != v[1]):
                targetX, targetY = i, j
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y, cnt = q.popleft()
        for dx in range(x - 1, -1, -1):
            if arr[dx][y] != 0 or dx == 0:
                if visited[dx][y] > cnt + 1:
                    q.append((dx, y, cnt + 1))
                    visited[dx][y] = cnt + 1
                break
        for dx in range(x + 1, 4):
            if arr[dx][y] != 0 or dx == 3:
                if visited[dx][y] > cnt + 1:
                    q.append((dx, y, cnt + 1))
                    visited[dx][y] = cnt + 1
                break
        for dy in range(y - 1, -1, -1):
            if arr[x][dy] != 0 or dy == 0:
                if visited[x][dy] > cnt + 1:
                    q.append((x, dy, cnt + 1))
                    visited[x][dy] = cnt + 1
                break
        for dy in range(y + 1, 4):
            if arr[x][dy] != 0 or dy == 3:
                if visited[x][dy] > cnt + 1:
                    q.append((x, dy, cnt + 1))
                    visited[x][dy] = cnt + 1
                break

        for move in moves:
            dx = x + move[0]
            dy = y + move[1]

            if 0 <= dx < 4 and 0 <= dy < 4 and visited[dx][dy] > cnt + 1:
                q.append((dx, dy, cnt + 1))
                visited[dx][dy] = cnt + 1
    return targetX, targetY
