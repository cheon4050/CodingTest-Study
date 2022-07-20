import sys
import collections
from typing import Tuple

n = int(sys.stdin.readline())
tree = collections.defaultdict(list)
for _ in range(n):
    start, *items, _ = list(map(int, sys.stdin.readline().split()))
    for i in range(0, len(items), 2):
        tree[start].append((items[i], items[i + 1]))

visited = [False] * (n + 1)
result = 0
def dfs(curr: Tuple[int]) -> int:
    distance = []
    visited[curr[0]] = True
    for next in tree[curr[0]]:
        if not visited[next[0]]:
            distance.append(dfs(next))
    global result
    if len(distance) == 1:
        result = max(result, distance[0])
    elif len(distance) >= 2:
        distance.sort(reverse=True)
        result = max(result, distance[0] + distance[1])
    return distance[0] + curr[1] if distance else curr[1]
dfs((1, 0))
print(result)