# 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램

def move(x, y, dir):    # 벽이나 구멍이 나올 때까지 방향 따라 쭉 이동
    cnt = 0
    while arr[x][y] != '#' and arr[x][y] != 'O':
        x += dx[dir]
        y += dy[dir]
        cnt += 1

    return x - dx[dir], y - dy[dir], cnt

def bfs():
    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10:
            # break   # 기울인 횟수가 10을 넘어가는 경로를 제외하고 아직 큐에 남아있는 다른 경로들에 답이 있을 수도 있으니 break X
            continue

        for dir in range(4):
            nrx, nry, r_move = move(rx, ry, dir)   # 빨간 구슬 굴리기
            nbx, nby, b_move = move(bx, by, dir)   # 파란 구슬 굴리기

            if arr[nbx + dx[dir]][nby + dy[dir]] == 'O':     # 빨간 구슬에 관계 없이 파란 구슬이 구멍에 떨어지는 상황이라면 실패
                continue

            if cnt < 10 and arr[nrx + dx[dir]][nry + dy[dir]] == 'O':    # 빨간 구슬이 구멍에 떨어진다면 먼저 도달하는게 최소 기울인 횟수이므로 리턴
                return cnt

            if nrx == nbx and nry == nby:           # 새로운 좌표가 빨간 구슬과 파란 구슬이 같다면 이동 거리가 큰 구슬을 뒤로 배치
                if r_move > b_move:
                    nrx -= dx[dir]
                    nry -= dy[dir]
                else:
                    nbx -= dx[dir]
                    nby -= dy[dir]

            if rx == nrx and bx == nbx and ry == nry and by == nby:  # 벽을 만나서 위치가 같은 경우 패스
                continue

            q.append([nrx, nry, nbx, nby, cnt + 1])   # 빨간 구슬이 구멍에 떨어지지 않는다면 계속해서 탐색을 이어나감
    return -1   # 반복문이 중간에 종료되지 않았다면 실패한 경우이므로 -1 리턴

from collections import deque

N, M = map(int, input().split())
q = deque()
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
red_x, red_y, blue_x, blue_y = 0, 0, 0, 0

arr = [["" for _ in range(M)] for _ in range(N)]
for i in range(N):
    temp = input()
    for j in range(M):
        arr[i][j] = temp[j]

        if temp[j] == 'R':    # R와 B의 위치 저장
            red_x, red_y = i, j
            arr[i][j] = '.'
        if temp[j] == 'B':
            blue_x, blue_y = i, j
            arr[i][j] = '.'

q.append([red_x, red_y, blue_x, blue_y, 0])  # 빨간 구슬과 파란 구슬 좌표, 기울인 횟수를 큐에 저장
print(bfs())