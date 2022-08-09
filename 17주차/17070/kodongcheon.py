import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
def dfs(x, y, direction):
    global result
    if x == N-1 and y == N-1:
        result += 1

    if x+1 < N and y+1 < N:
        if arr[x+1][y+1] == 0 and arr[x+1][y] == 0 and arr[x][y+1] == 0:
            dfs(x+1, y+1, 2)

    if direction == 0 or direction == 2:
        if y + 1 < N:
            if arr[x][y + 1] == 0:
                dfs(x, y + 1, 0)

    if direction == 1 or direction == 2:
        if x + 1 < N:
            if arr[x + 1][y] == 0:
                dfs(x + 1, y, 1)

dfs(0, 1, 0)

print(result)


