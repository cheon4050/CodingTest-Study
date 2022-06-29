from collections import deque

N, M = map(int, input().split())

arr = {}
for i in range(N+M):
    x, y = map(int,input().split())
    arr[x] = y

queue = deque([(1,1)])
dp = [100]*101
visited = [False] * 101
while(queue):
    start, cnt = queue.popleft()
    for i in range(1,7):
        c = 0
        if start+i == 101:
            break
        elif start+i in arr:
            dp[arr[i+start]] = min(cnt, dp[arr[i+start]])
            c = arr[i+start]
        else:
            dp[start+i] = min(cnt, dp[start+i])
            c = start+i
        if visited[c] == True:
            continue
        queue.append((c,cnt+1))
        visited[c] = True
print(dp[-1])



