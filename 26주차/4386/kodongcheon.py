def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v =int(input())

parent = [0] * (v+1)

edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i

arr = [list(map(float, input().split()))for i in range(v)]

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        edges.append(((abs(arr[i][0] - arr[j][0]) ** 2 + abs(arr[i][1] - arr[j][1]) ** 2) ** (1 / 2),i, j))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)