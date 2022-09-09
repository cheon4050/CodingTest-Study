import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int,input().split())

arr = []
queue = deque()
for i in range(H):
    temp1 = []
    for j in range(N):
        temp2 = list(map(int, input().split()))
        temp1.append(temp2)
        for k in range(M):
            if temp2[k] == 1:
                queue.append((i, j, k))
    arr.append(temp1)

# 1의 위치값 큐에 저장

di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]
maxcnt = 1

# BFS 코드
while queue:
    i, j, k = queue.popleft()
    for n in range(6):
        ti = i + di[n]
        tj = j + dj[n]
        tk = k + dk[n]
        if 0 <= ti < H and 0 <= tj < N and 0 <= tk < M and arr[ti][tj][tk] == 0:
            arr[ti][tj][tk] = arr[i][j][k] + 1
            maxcnt = max(maxcnt, arr[ti][tj][tk])
            queue.append((ti, tj, tk))

#익지 않은 토마토 찾기
breaker = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 0:
                print(-1)
                breaker = True
                break
        if breaker:
            break
    if breaker:
        break
else:
    print(maxcnt-1)