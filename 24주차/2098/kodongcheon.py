def req(now, visited):
    if DP[now][visited]:
        return DP[now][visited]

    if visited == (1<<N) -1:
        if arr[now][0]:
            return arr[now][0]
        else:
            return INF

    cost = INF
    for i in range(1,N):
        if not visited & (1 << i) and arr[now][i]:
            tmp = req(i, visited | (1<<i))
            cost = min(cost, tmp+arr[now][i])
    DP[now][visited] = cost
    return DP[now][visited]

INF = 100000000

N = int(input())
arr = [list(map(int, input().split()))for i in range(N)]
DP = [[0] * (1<<N) for i in range(N)]

print(req(0, 1))