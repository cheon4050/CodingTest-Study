def solution(n, wires):
    result = []
    for i in range(n-1):
        temp = wires[:i] + wires[i+1:]
        arr = [[] for _ in range(n+1)]
        visited = [False] * (n+1)
        for v1, v2 in temp:
            arr[v1].append(v2)
            arr[v2].append(v1)
        cnt = dfs(1, arr, visited)+1
        result.append(abs((n-2*cnt)))

    return min(result)

def dfs(v, arr, visited):
    visited[v] = True
    cnt = 0
    if not arr[v]:
        return 0
    for i in arr[v]:
        if not visited[i]:
            cnt += 1
            cnt += dfs(i, arr, visited)
    return cnt