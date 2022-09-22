import sys
sys.setrecursionlimit(100000)
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
def solution(n, paths, gates, summits):
    paths.sort(key = lambda x : x[-1])
    parent = [0] * (n+1)
    graph = [[]for i in range(n+1)]
    for i in range(1, n+1):
        parent[i] = i
    for path in paths:
        a, b, cost = path

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            graph[a].append([b, cost])
            graph[b].append([a, cost])
    result = []
    global max_value
    max_value = 1000000000
    for gate in gates:
        visited = [False] * (n+1)
        dfs(graph, gate, visited, summits, result, 0, gates)
    return sorted(result, key = lambda x : (x[1], x[0]))[0]

def dfs(graph, v, visited, summits, result, cnt, gates):
    global max_value
    visited[v] = True
    if max_value < cnt:
        return
    if cnt != 0 and v in gates:
        return
    if v in summits:
        max_value =  cnt
        result.append([v, cnt])
        return
    for i in graph[v]:
        if not visited[i[0]]:
            cnt = max(cnt, i[1])
            dfs(graph,i[0],visited, summits, result, cnt, gates)