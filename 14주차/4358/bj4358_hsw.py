import sys
import collections

seen = collections.defaultdict(int)
while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    seen[tree] += 1
for tree in sorted(seen.keys()):
    print("%s %.4f" %(tree, seen[tree] / sum(seen.values()) * 100.0))