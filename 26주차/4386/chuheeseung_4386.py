import sys
input = sys.stdin.readline

# union - find : 사이클을 판단하기 위함
def union(a, b): # a, b를 합치는 함수
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def find(a): # a의 부모 노드를 찾는 함수
    if a == parent[a]:
        return a
    else:
        return find(parent[a])

n = int(input()) # 별의 개수 n
stars = [list(map(float, input().split())) for _ in range(n)]
parent = [_ for _ in range(n)] # 각 정점의 부모 노드를 나타내는 배열
costs = {} # {(별1, 별2) : distance} 형태

for i in range(n): # 간선들의 비용을 계산하여 costs에 저장
    for j in range(i + 1, n):
        a = stars[i]
        b = stars[j]
        distance = round(((a[0]-b[0]) ** 2 + (a[1]-b[1]) ** 2) ** 0.5, 2)
        costs[(i, j)] = distance

costs = sorted(costs.items(), key = lambda x: x[1]) # 크루스칼 알고리즘 쓰기 위해 distance를 오름차순으로 정렬

# 크루스칼 알고리즘
answer = 0

while costs:
    current = costs.pop(0)
    a, b = current[0]
    cost = current[1]

    if find(a) != find(b): # 같은 그룹에 있는게 아닌 경우
        answer += cost
        union(a, b)

print(answer)

