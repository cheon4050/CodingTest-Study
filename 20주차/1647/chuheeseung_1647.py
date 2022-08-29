import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [0] * (n + 1)
rank = [0] * (n + 1)
edges = [[] for i in range(m + 1)]

for i in range(1, n + 1):
    parent[i] = i

for i in range(1, m + 1):
    a, b, c = map(int, input().split())
    edges[i].extend([c, a, b])

def find(a):
    if parent[a] == a:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = parent[a]
    b = parent[b]
    if a == b:
        return
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1


def kruskal(edges):
    edges.sort()
    cost = 0
    mst = []

    for edge in edges:
        if not edge:
            continue
        c, a, b = edge

        if find(a) != find(b):
            union(a, b)
            cost += c
            mst.append([a, b])
            if len(mst) == n - 2:
                return cost

    return cost

print(kruskal(edges))