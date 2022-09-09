import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [0, 0]
def check(x, y, k, arr, result):
    for i in range(x, x+k):
        for j in range(y, y+k):
            if arr[i][j] != arr[x][y]:
                k = k//2
                check(x, y, k, arr, result)
                check(x, y+k, k, arr, result)
                check(x+k, y, k, arr, result)
                check(x+k, y+k, k, arr, result)
                return
    result[arr[x][y]] += 1

check(0, 0, N, arr, result)
print(*result, sep='\n')
