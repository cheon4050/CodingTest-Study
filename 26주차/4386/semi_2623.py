# 별자리를 만드는 최소 비용 구하기 : 최소 스패닝 트리(크루스칼 알고리즘)

import math
from itertools import combinations


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    print(a, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
arr = [list(map(float, input().split())) for _ in range(N)]
visited = [False] * N
edges = []
parent = [0] * (N+1)    # 부모 노드 정보가 담길 테이블

for pair in combinations(arr, 2):  # 모든 간선 데이터 + 비용 배열 생성
    i = arr.index(pair[0])
    j = arr.index(pair[1])

    x1, y1, x2, y2 = pair[0][0], pair[0][1], pair[1][0], pair[1][1]
    d = round(math.sqrt(abs(x2 - x1) ** 2 + abs(y1 - y2) ** 2), 2)  # 거리
    edges.append([i+1, j+1, d])

edges.sort(key=lambda x: x[2])  # 간선 데이터를 비용에 따라 오름차순으로 정렬

for i in range(1, N+1):   # 사이클 판별을 위해 parent 배열 초기화
    parent[i] = i

result = 0
for edge in edges:
    a, b, cost = edge

    if find_parent(parent, a) != find_parent(parent, b):   # 사이클 발생하지 않은 경우에만 집합에 포함
        union_parent(parent, a, b)
        result += cost
print(result)