import sys
sys.setrecursionlimit(10**5) # 재귀 호출 횟수를 늘려준다
input = sys.stdin.readline

n = int(input()) # 노드 개수
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)] # 부모를 저장하는 리스트

for _ in range(n - 1): # 트리 저장
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def check(start, end, parents):
    for i in tree[start]: # 연결된 노드를 모두 탐색
        if parent[i] == 0: # 한번도 방문한 적이 없는 경우
            parent[i] = start # 부모 노드를 저장
            check(i, tree, parent)


check(1, tree, parent)

for i in range(2, n + 1):
    print(parent[i])