import sys

def dfs(r: int, c: int, count: int):
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < n and 0 <= dc < m and not seen[words[dr][dc]]:
            seen[words[dr][dc]] = True
            dfs(dr, dc, count + 1)
            seen[words[dr][dc]] = False
    global result
    result = max(result, count)

n, m = map(int, sys.stdin.readline().split())
words = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(n)]
seen = [False for _ in range(26)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
result = 0
seen[words[0][0]] = True
dfs(0, 0, 1)
print(result)