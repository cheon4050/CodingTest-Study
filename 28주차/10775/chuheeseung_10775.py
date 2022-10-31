import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
parent = [i for i in range(g + 1)]
arr = [int(input()) for _ in range(p)]
answer = 0

def find(curr):
    if parent[curr] == curr:
        return curr

    parent[curr] = find(parent[curr])

    return parent[curr]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

for g in arr:
    p = find(g)

    if p == 0:
        break
    
    answer += 1
    union(p-1, p)

print(answer)