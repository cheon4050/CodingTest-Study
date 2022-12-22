# 낚시왕이 잡은 상어 크기의 합 구하기
def move_shrek(x, y, v, dir):
    while 0 < v:
        nx, ny = x + dx[dir], y + dy[dir]    # 이동 시키지 않고 다음 좌표만 구하기
        if 1 <= nx <= R and 1 <= ny <= C:    # 다음 좌표가 맵 안인 경우 이동 시키기
            x, y = nx, ny
            v -= 1                # 이동 해야할 남은 거리 차감
        else:
            if dir == 1 or dir == 3:       # 다음 좌표가 맵을 벗어 난다면 방향만 반대로 바꿔 주기
                dir += 1
            else:
                dir -= 1
    return x, y, dir

R, C, M = map(int, input().split())
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, 1, -1]    # 위 아래 오른쪽 왼쪽
board = [[0 for _ in range(C + 1)] for _ in range(R + 1)]  # 상어의 위치가 저장 되는 배열
user_y = 1         # 낚시꾼 위치
shrek_size = 0      # 잡은 상어 크기의 합

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = (s, d, z)

while user_y <= C:      # 낚시꾼의 위치
    caught = False
    temp_board = [[0 for _ in range(C + 1)] for _ in range(R + 1)]  # 원본 상어의 위치를 해치지 않기 위해 임시 보드를 생성(이동 시켜야 할 상어를 먹어 버리는 경우 방지)
    for i in range(1, C + 1):
        for j in range(1, R + 1):
            if board[j][i] == 0:   # 해당 칸에 상어가 존재 하지 않는 경우
                continue

            if not caught and i == user_y:    # 낚시꾼의 위치와 가장 가까운 상어 잡기
                shrek_size += board[j][i][2]
                board[j][i] = 0
                caught = True
            else:               # 나머지 상어 모두 이동 시키기
                s, d, z = board[j][i][0], board[j][i][1], board[j][i][2]
                nx, ny, dir = move_shrek(j, i, s, d)    # 바뀐 위치와 방향 저장
                if temp_board[nx][ny] == 0 or z > temp_board[nx][ny][2]:  # 아무도 없거나 기존에 존재하던 상어의 크기보다 큰 경우에만 덮어씌우기
                    temp_board[nx][ny] = (s, dir, z)
    board = temp_board    # 모두 이동 시킨 상어의 최종 위치를 원본 보드에 덮기
    user_y += 1
print(shrek_size)


