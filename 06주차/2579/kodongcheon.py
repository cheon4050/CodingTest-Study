import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    num = int(input())
    arr.append(num)

visited = [0] * N
if N < 3:
    print(sum(arr))
else:
    visited[2] = max(arr[0]+arr[2], arr[1]+arr[2])
    visited[1] = arr[1]+arr[0]
    visited[0] = arr[0]
    for i in range(3, N):
        visited[i] = max(visited[i-3]+arr[i-1]+arr[i], visited[i-2]+arr[i])

    print(visited[-1])

