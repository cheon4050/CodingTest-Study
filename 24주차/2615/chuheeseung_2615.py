import sys
input = sys.stdin.readline

def bfs(x, y):
    target = graph[x][y] # 바둑알의 색 (검1, 흰2)

    for k in range(4): # 4가지 방향으로 탐색
        cnt = 1 # 바둑알 개수
        nx = x + dx[k]
        ny = y + dy[k]

        # while 문을 통해서 오목이 되는지 확인
        # 범위 안에 있고 target과 색이 동일한 경우
        while 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == target:
            cnt += 1

            if cnt == 5: # 오목인 경우
                # 육목인지 아닌지 확인 -> 육목은 이긴게 아님
                if 0 <= x - dx[k] < 19 and 0 <= y - dy[k] < 19 and graph[x-dx[k]][y-dy[k]] == graph[x][y]:
                    # 육목 판정 1 : 제일 처음 좌표랑 해당 좌표에서 (-dx[k], -dy[k]) 만큼 이동한 좌표가 같은지 확인
                    break

                if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and graph[nx+dx[k]][ny+dy[k]] == graph[nx][ny]:
                    # 육목 판정 2 : 제일 마지막 좌표에서 (+dx[k], +dy[k]) 만큼 이동한 좌표가 같은지 확인
                    break

                print(target) # 육목이 아니면 성공한 것으로 판단해서 바둑알의 색과 위치 출력
                print(x + 1, y + 1)
                exit(0)

            nx += dx[k] # 방향 다시 이동
            ny += dy[k]

graph = [list(map(int, input().split())) for _ in range(19)]

# → ↓ ↘ ↗ # 위에서 오른쪽으로 탐색하니까 이 방향으로만 탐색을 해도 된다
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for i in range(19): # 반복문을 통해서 바둑알의 위치를 탐색
    for j in range(19):
        if graph[i][j] != 0: # 바둑알이 있는 경우
            bfs(i, j)

print(0)