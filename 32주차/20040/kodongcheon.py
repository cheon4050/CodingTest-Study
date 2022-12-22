import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(M):
    x = map(int, input().split())
    arr.append(x)

def find(parent, x):
    if parent[x] != x:
        parent[x] =find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return False
    if a < b:
        parent[b] = a
        return True
    else:
        parent[a] = b
        return True

parent = [0] * (N)

for i in range(N):
    parent[i] = i

cnt = 0
for a, b in dict.fromkeys(arr):
    cnt += 1
    if not union(parent, a, b):
        break
else:
    cnt = 0
print(cnt)


