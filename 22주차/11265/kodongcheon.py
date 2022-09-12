import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
            # arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

for i in range(M):
    A, B, C = map(int,input().split())

    if arr[A-1][B-1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")