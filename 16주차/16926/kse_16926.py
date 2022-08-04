N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# N, M의 최소값으로 1회전 시 돌아야 하는 곳 체크
cnt = min(N, M) // 2

for _ in range(R):
    temp = 0
    x, y = 0, 0
    while temp < cnt:
        nx = x + temp
        ny = y + temp
        # 상 -> 하
        value = arr[nx][ny]
        for i in range(nx+1, N-temp):
            prev = arr[i][ny]
            arr[i][ny] = value
            value = prev
        # 좌 -> 우
        for j in range(ny+1, M-temp):
            prev = arr[N-temp-1][j]
            arr[N-temp-1][j] = value
            value = prev
        # 하 -> 상
        for i in range(N-temp-2, nx-1, -1):
            prev = arr[i][M-1-temp]
            arr[i][M-1-temp] = value
            value = prev
        # 우 -> 좌
        for j in range(M-temp-2, ny-1, -1):
            prev = arr[nx][j]
            arr[nx][j] = value
            value = prev
        temp += 1
for item in arr:
    print(*item)
