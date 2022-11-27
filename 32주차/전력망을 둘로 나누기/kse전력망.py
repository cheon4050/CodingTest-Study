from collections import deque
#bfs
def bfs(start, visited, graph):
    q = deque([start])
    result = 1
    visited[start] = True
    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i] == False:
                result += 1
                q.append(i)
                visited[i] = True
    return result

def solution(n, wires):
    answer = n
    arr = [[] for _ in range(n+1)]

    for i,j in wires:
        arr[i].append(j)
        arr[j].append(i)

    for start, not_visit in wires:
        visited = [False]*(n+1)
        visited[not_visit] = True # 전력망을 나누는 기준
        result = bfs(start, visited, arr)
        if abs(result - (n-result)) < answer :
            answer = abs(result - (n-result))

    return answer