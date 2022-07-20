import sys
input = sys.stdin.readline
d = {}
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    d[tree] = d.get(tree, 0)+1
    n += 1
for k in sorted(d):
    print("%s %.4f" % (k, d[k]/n*100))
