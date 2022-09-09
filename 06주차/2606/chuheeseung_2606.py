from collections import defaultdict

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드 방문했다고 처리

    for i in graph[v]: # 현재 노드와 연결된 다른 노드들 방문
        if not visited[i]:
            dfs(graph, i, visited)

    return visited.count(True) - 1 # 1번은 제외해야 해서 -1


n = int(input()) # 컴퓨터 개수
m = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = defaultdict(list)

for _ in range(m): # 입력 받아서 그래프 생성
    a, b = map(int, input().split()) # a: 컴퓨터 번호, b: 연결된 컴퓨터들
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1) # 각 노드가 방문한 정보를 리스트에 담음 (F:미방문, T:방문)

print(dfs(graph, 1, visited))