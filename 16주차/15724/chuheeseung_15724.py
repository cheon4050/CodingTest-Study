import sys
input = sys.stdin.readline

n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
sum = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1): # 누적합
    for j in range(1, m + 1):
        sum[i][j] = area[i-1][j-1] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

for _ in range(k): # 각 구역의 영역합 출력
    x, y, i, j = map(int, input().split())
    print(sum[i][j] - sum[x-1][j] - sum[i][y-1] + sum[x-1][y-1])