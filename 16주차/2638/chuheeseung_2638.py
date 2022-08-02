import sys
from collections import deque
input = sys.stdin.readline

def checkOutSideAir(): # 바깥 공기를 -1로 초기화하는 함수
    q = deque()
    out_visited = [[False] * m for _ in range(n)] # 방문 여부 저장하는 리스트
    q.append((0, 0))
    out_visited[0][0] = True
    checkBoard[0][0] = -1 # 가장자리는 치즈가 놓이지 않는다고 가정했으니까 -1로 초기화

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x

            if ny < 0 or ny >= n or nx < 0 or nx >= m: # 리스트의 범위를 초과하는 경우 예외
                continue

            if checkBoard[ny][nx] == 1 or out_visited[ny][nx]: # 모눈종이에 치즈가 있거나 이미 방문한 경우
                continue

            q.append((ny, nx))
            checkBoard[ny][nx] = -1 # 외부 치즈와 맞닿은 공기만 -1로 수정
            out_visited[ny][nx] = True # 방문했다고 표시

    return

def isMelt(): # 치즈가 다 녹았는지 확인하는 함수
    for i in range(n):
        for j in range(m):
            if checkBoard[i][j] == 1: # 치즈가 남아있는 경우
                return False

    return True


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
checkBoard = [list(map(int, input().split())) for _ in range(n)] # 모눈종이 리스트
answer = 0

while not isMelt(): # 치즈가 다 녹을 때까지 반복
    checkOutSideAir() # 외부 공기를 -1로 초기화
    check = [] # 외부 공기랑 맞닿은 칸을 저장하는 리스트

    for i in range(n):
        for j in range(m):
            if checkBoard[i][j] == 1: # 모눈종이에 치즈가 있는 경우
                count = 0 # 외부 공기와 맞닿은 칸의 개수를 저장하는 변수

                for k in range(4): # 4방향 탐색
                    ny = dy[k] + i
                    nx = dx[k] + j

                    if ny < 0 or ny >= n or nx < 0 or nx >= m: # 리스트의 범위를 초과하는 경우 예외
                        continue

                    if checkBoard[ny][nx] == -1: # 외부 공기와 맞닿은 경우
                        count += 1

                if count >= 2: # 변이 2개 이상 맞닿아야 녹을 수 있음
                    check.append([i, j])

    for y, x in check: # 외부부공기랑 맞닿은 칸은 녹음
        checkBoard[y][x] = 0 # 치즈가 없다고 리스트 값 수정

    answer += 1 # 한시간이 지났으니까 +1

print(answer)

# 모든 치즈가 다 녹았는지 확인, 남아있으면 while문 반복
# 내부공간에 있지 않는 치즈들 중 외부 공기와 2변 이상 접촉한 치즈 체크
# 체크된 치즈를 녹인다

# 외부 공기를 따로 처리하는 로직이 필요 (녹고 나서 외부 공기랑 2변 이상 맞닿는 경우)
    # 2차원 리스트를 돌면서 4변 탐색
    # 다음 진행방향이 치즈면 큐에 넣음
    # 큐에 들어간 좌표는 리스트에서 -1로 업데이트
    # => 내부 치즈와 맞닿은 공기들은 0, 외부 치즈와 맞닿은 공기는 -1