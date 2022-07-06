import sys
import collections
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
result = [0 for _ in range(n + 1)]
tree = collections.defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(parent: int, curr: int) -> None:
    result[curr] = parent
    for next in tree[curr]:
        if not result[next]:
            dfs(curr, next)
dfs(1, 1)
print(*result[2:], sep='\n')