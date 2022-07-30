import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
sumArr = [[0] * M for i in range(N)]
for i in range(N):
    sumArr[i][0] = arr[i][0]
for i in range(N):
    for j in range(1,M):
        sumArr[i][j] = sumArr[i][j-1] + arr[i][j]
for j in range(M):
    for i in range(1,N):
        sumArr[i][j] += sumArr[i-1][j]

K = int(input())

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
    if x1 == 0 and y1 == 0:

        print(sumArr[x2][y2])
    elif x1 == 0:
        print(sumArr[x2][y2] - sumArr[x2][y1-1])
    elif y1 == 0:
        print(sumArr[x2][y2] - sumArr[x1-1][y2])
    else:
        print(sumArr[x2][y2] - sumArr[x2][y1 - 1]- sumArr[x1-1][y2] + sumArr[x1-1][y1-1])
