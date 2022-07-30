import sys
input = sys.stdin.readline
N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

sumArr = [[0]* (N-2) for _ in range(N-2)]

for i in range(1, N-1):
    for j in range(1, N-1):
        sumArr[i-1][j-1] = arr[i][j] + arr[i-1][j] + arr[i+1][j] + arr[i][j-1] + arr[i][j+1]

result = 1000000
for i in range(N-2):
    for j in range(N-2):
        for x in range(N-2):
            for y in range(N-2):
                for a in range(N - 2):
                    for b in range(N - 2):
                        if abs(x-i) + abs(y-j) > 2 and abs(a-i) + abs(b-j) > 2 and abs(x-a) + abs(y-b) > 2:
                            result = min(result, sumArr[i][j]+sumArr[x][y]+sumArr[a][b])
print(result)