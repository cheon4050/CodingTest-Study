import sys
input = sys.stdin.readline
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent,a)
    b = find(parent,b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())

    edges.append((cost, a, b))

edges.sort()
maxCost = 0
for edge in edges:
    cost, a, b = edge

    if find(parent,a) != find(parent, b):
        union(parent, a, b)
        result += cost
        maxCost = max(maxCost, cost)
print(result-maxCost)
