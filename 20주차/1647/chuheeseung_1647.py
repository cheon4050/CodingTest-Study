import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split()) # 노드 수 : n, 간선 수 : m
parent = [0] * (n + 1) # 부모 노드를 저장할 공간
rank = [0] * (n + 1) # 집합의 rank를 저장할 공간
edges = [[] for i in range(m + 1)] # 간선의 정보를 저장할 공간

for i in range(1, n + 1): # 부모 노드를 자기 자신으로 설정
    parent[i] = i

for i in range(1, m + 1):
    a, b, c = map(int, input().split()) # a집과 b집을 연결하는 길의 유지비가 c
    edges[i].extend([c, a, b])

# union find 알고리즘
def find(a):
    if parent[a] == a: # 자기 자신이 부모노드인 경우
        return a
    p = find(parent[a]) # 부모 노드 탐색
    parent[a] = p # 부모 노드 갱신
    return parent[a]

def union(a, b): # 두 분리 집합 병합
    a = parent[a] # 부모 노드 얻기
    b = parent[b] # 부모 노드 얻기
    if a == b: # 동일한 집합에 속하는 경우
        return
    if rank[a] > rank[b]: # 작은 집합을 큰 집합에 병합
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

# kruskal 알고리즘
def kruskal(edges):
    edges.sort() # 가중치 기준으로 정렬
    cost = 0 # 비용
    mst = [] # 최소 신장 트리

    for edge in edges:
        if not edge: # 0번 인덱스 edge 생략
            continue
        c, a, b = edge

        if find(a) != find(b): # 분리 집합이면 병합
            union(a, b)
            cost += c
            mst.append([a, b])
            if len(mst) == n - 2: # 그래프를 두개의 집합으로 분리하기 위해 중지하는 조건
                return cost

    return cost

print(kruskal(edges))