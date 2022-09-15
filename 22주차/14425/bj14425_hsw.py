import sys

n, m = map(int, sys.stdin.readline().split())
table = set()
for _ in range(n):
    table.add(sys.stdin.readline().rstrip())
count = 0
for _ in range(m):
    if sys.stdin.readline().rstrip() in table:
        count += 1
print(count)