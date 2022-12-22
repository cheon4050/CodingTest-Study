import sys
sys.setrecursionlimit(10000)

def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x

    # if parent[x] != x:   # 반복문을 사용한 방법이랑 시간 차이는 별로 나지 않음
    #     parent[x] = find_parent(parent[x])
    # return parent[x]

def union(a, b):
    pa = find_parent(a)
    pb = find_parent(b)

    if pa > pb:
        parent[pa] = pb
    else:
        parent[pb] = pa

N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    if find_parent(a + 1) == find_parent(b + 1):  # 부모가 같아서 사이클이 발생한 경우 중단
        print(i + 1)
        break
    else:
        union(a + 1, b + 1)     # 사이클이 발생하지 않은 경우 두 노드를 합치기
else:           # m 번의 차례를 모두 처리한 이후에도 죵료되지 않은 경우
    print(0)
