import sys
sys.setrecursionlimit(1000000)

def solution(grid):
    N = len(grid)
    M = len(grid[0])
    visited = [[[False] * 4 for i in range(M)] for j in range(N)]
    result = []
    for i in range(N):
        for j in range(M):
            for k in range(4):
                if not visited[i][j][k]:
                    result.append(dfs(i, j, k, visited, grid, 0))
    return sorted(result)

def dfs(x, y, command, visited, arr, cnt):
    if visited[x][y][command] == True:
        return cnt

    visited[x][y][command] = True

    if arr[x][y] == "L":
        command = (command + 1) % 4
    elif arr[x][y] == "R":
        command = (command - 1) % 4
    # 위
    if command == 0:
        x = (x - 1) % len(arr)
    # 왼쪽
    elif command == 1:
        y = (y - 1) % len(arr[0])
    # 아래
    elif command == 2:
        x = (x + 1) % len(arr)
    # 오른쪽
    elif command == 3:
        y = (y + 1) % len(arr[0])

    return dfs(x, y, command, visited, arr, cnt + 1)

