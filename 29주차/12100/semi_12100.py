# 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값을 구하는 프로그램

import copy


def dfs(dir):
    flag = [[False for _ in range(N)] for _ in range(N)]

    # 움직이는 방향에 따라 업데이트 해야하는 좌표의 순서가 달라짐
    # 이동 방향의 벽면 쪽에 먼저 붙는 노드들 부터 처리 해야 하기 때문에
    if dir == 1 or dir == 3:
        start, end, step = 0, N, 1   # 위 / 왼쪽일 경우 왼쪽 위 -> 오른쪽 아래 방향
    else:
        start, end, step = N-1, -1, -1  # 아래 / 오른쪽일 경우 오른쪽 아래 -> 왼쪽 위 방향

    for a in range(start, end, step):
        for b in range(start, end, step):
            x, y = a, b  # 복사

            if game[x][y] == 0:   # 애초에 옮기려는 수가 없다면 종료
                continue

            nx, ny = x + dx[dir], y + dy[dir]   # 해당 방향으로 한칸 위로 이동한 위치

            if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 범위 벗어 나는 경우
                continue

            while True:
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break

                if not flag[nx][ny] and game[x][y] == game[nx][ny]:  # 합쳐지지 않았고 숫자가 같은경우 합치기
                    game[nx][ny] += game[x][y]
                    game[x][y] = 0
                    flag[nx][ny] = True     # 합쳐진 경우는 다시 합쳐지지 않도록 설정
                    break              # 합쳐진 이후에 다음 노드의 수가 같은 경우 합쳐지지 않도록 한번 합쳐진다면 바로 반복문 종료

                elif game[nx][ny] == 0:     # 빈칸인 경우 그냥 이동
                    game[nx][ny] = game[x][y]
                    game[x][y] = 0

                else:
                    break

                x, y = nx, ny
                nx, ny = nx + dx[dir], ny + dy[dir]


def move(depth):
    global game, result
    if depth == 5:
        for k in range(N):
            result = max(result, max(game[k]))  # 이동하고 난 배열의 가장 큰 값 찾기
        return

    arr = copy.deepcopy(game)  # 원본 배열의 상태 유지
    for j in range(4):    # 네 방향 이동
        dfs(j)
        move(depth + 1)
        game = copy.deepcopy(arr)    # 재귀 종료시(한 가지가 끝났을 경우) 원본 배열로 복구


N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
result = 0
move(0)
print(result)