import sys
input = sys.stdin.readline

def dfs(x, y, shape):
    global answer

    if x == n-1 and y == n-1: # (n-1, n-1)에 파이프가 도착하면 횟수 +1 증가
        answer += 1
        return

    if shape == 0 or shape == 2: # 가로는 가로, 대각선 두가지 방법
        if y + 1 < n:
            if a[x][y+1] == 0: # 다음 칸이 빈칸이면 dfs 호출
                dfs(x, y+1, 0)

    if shape == 1 or shape == 2: # 세로는 세로, 대각선 두가지 방법
        if x + 1 < n:
            if a[x+1][y] == 0: # 다음 칸이 빈칸이면 dfs 호출
                dfs(x+1, y, 1)

    if shape == 0 or shape == 1 or shape == 2: # 대각선은 가로, 세로, 대각선 세가지 방법
        if x + 1 < n and y + 1 < n:
            if a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0: # 다음 칸이 빈칸이면 dfs 호출
                dfs(x+1, y+1, 2)

n = int(input()) # 집의 크기
a = [list(map(int, input().split())) for _ in range(n)] # 집의 상태 (칸0, 벽1)
answer = 0
dfs(0, 1, 0) # (0,1) 좌표, shape 변수 (0:가로, 1:세로, 2:대각선)
# 처음이 (1,1), (1,2)에 있는데 0부터 땡김
# 가로로 있으니까 함수에 shape 변수로 0 넣어줌
print(answer)