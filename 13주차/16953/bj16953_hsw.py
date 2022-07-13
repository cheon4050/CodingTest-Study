import sys
import collections

a, b = map(int, sys.stdin.readline().split())

def bfs(curr: int) -> int:
    queue = collections.deque([(curr, 1)])
    while queue:
        curr, count = queue.popleft()
        if curr == b:
            return count
        for next in [int(str(curr) + '1'), curr * 2]:
            if next >= 1 and next <= 1000000000:
                queue.append((next, count + 1))
    return -1
print(bfs(a))