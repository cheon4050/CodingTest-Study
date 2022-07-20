import sys
from collections import defaultdict

input = sys.stdin.readline

tree = defaultdict(int)

cnt = 0
while True:
    name = input().rstrip()
    if name == "":
        break
    tree[name] += 1
    cnt += 1
tname = list(tree.keys())
tname.sort()

for n in tname:
    print("%s %.4f" % (n, tree[n] * 100 / cnt))
