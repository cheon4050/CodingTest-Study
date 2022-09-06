import sys
input = sys.stdin.readline

R, C = map(int, input().split())

arr = []
for _ in range(R):
    arr.append(input().rstrip())

result = 0
def dfs(x, y, temp):
    global result
    moves = [(-1,0), (1, 0), (0, -1), (0, 1)]
    result = max(result, len(temp))
    for move in moves:
        dx = move[0] + x
        dy = move[1] + y

        if 0 <= dx < R and 0 <= dy < C and not arr[dx][dy] in temp:
            dfs(dx,dy,(temp+arr[dx][dy])[:])
dfs(0, 0, arr[0][0])
print(result)
