import sys
from collections import deque
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
KList = list(map(int, input().split()))
QList = list(map(int, input().split()))
arr = [list(map(int,input().split()))for i in range(M)]
checkList = [False]*(N+3)
dp = [0]*(N+3)
visited = [False] * (N+3)
q = deque(QList)
while q:
    v = q.popleft()
    if v in KList:
        continue
    visited[v]=True
    checkList[v]=True
    temp = v
    while temp <= N + 2:
        if v in KList:
            break
        if not visited[temp]:
            q.append(temp)
            visited[temp] = True
            checkList[v] = True
        temp+=v
for i in range(3, N+3):
    dp[i] += dp[i-1]
    if checkList[i]:
        dp[i] +=1
for S,E in arr:
    print(E-S-dp[E]+dp[S-1]+1)