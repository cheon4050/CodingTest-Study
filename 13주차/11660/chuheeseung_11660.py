import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
sumData = [[0] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sumData[i][j] = sumData[i][j-1] + sumData[i-1][j] - sumData[i-1][j-1] + data[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(sumData[x2][y2] - sumData[x1-1][y2] - sumData[x2][y1-1] + sumData[x1-1][y1-1])

# 전체 - 사이드 빼줄 곳 - 사이드 빼줄 곳 + 두번 빼줘서 한번 더할 곳 = 구할 곳