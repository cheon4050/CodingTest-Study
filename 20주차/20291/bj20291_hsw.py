import sys
import collections

n = int(sys.stdin.readline())
files = collections.defaultdict(int)
for _ in range(n):
    _, extension = map(str, sys.stdin.readline().rstrip().split('.'))
    files[extension] += 1
result = sorted(files.items(), key=lambda x: x[0])
for file in result:
    print(*file)