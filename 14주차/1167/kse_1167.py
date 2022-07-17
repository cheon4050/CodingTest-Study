from collections import deque

# 트리의 정점의 개수 v
v = int(input())
graph = [[] for _ in range(v + 1)]

# 간선의 정보: 정점번호, 정점번호, 정점까지의 거리
for _ in range(v):
    li = list(map(int, input().split()))
    for i in range(1, len(li) - 2, 2):
        # graph[정점].append((연결된 정점, 거리))
        graph[li[0]].append((li[i], li[i + 1]))

# 정점에서 가장 먼 거리(정점) 찾기
def bfs(start):
    global v
    q = deque()
    # 아직 방문하지 않은 노드는 visited[node] = -1
    visited = [-1] * (v + 1)
    # [노드까지의 거리, 노드]
    max = [0, 0]
    visited[start] = 0
    q.append(start)
    while q:
        now = q.popleft()
        for v2, e in graph[now]:
            if visited[v2] == -1: # 방문하지 않은 노드일 경우에는
                visited[v2] = visited[now] + e # 노드 거리 더해서 수정
                q.append(v2)
                # start 노드에서부터 가장 먼 거리의 노드
                if max[0] < visited[v2]:
                    max = visited[v2], v2

    return max

# 아무 노드 선택 -> 1
dis, node = bfs(1)
dis, node = bfs(node)
print(dis)