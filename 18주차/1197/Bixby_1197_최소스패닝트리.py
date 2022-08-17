import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    parent[max(a, b)] = min(a, b)
    return


v, e = map(int, input().split())

parent = [i for i in range(v+1)]
tree = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    tree.append((cost, a, b))
tree.sort()

result = 0
for cost, a, b in tree:
    if find(a) != find(b):
        union(a, b)
        result += cost
print(result)
